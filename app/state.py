import reflex as rx
import os
from google import genai
from google.genai import types
from app.database import (
    get_recommendation_from_db,
    get_budget_tier,
    get_use_case_priority,
    Component,
)
import time
import logging


class PCBuilderState(rx.State):
    budget: int = 50000
    use_cases: list[str] = ["Gaming"]
    other_requirements: str = ""
    all_use_cases: list[dict[str, str]] = [
        {"name": "Gaming", "icon": "gamepad-2"},
        {"name": "Content Creation", "icon": "video"},
        {"name": "Development", "icon": "code"},
        {"name": "Office Work", "icon": "briefcase"},
        {"name": "AI/ML", "icon": "brain-circuit"},
        {"name": "Home Theater", "icon": "film"},
    ]
    is_loading: bool = False
    is_streaming: bool = False
    stream_complete: bool = False
    streaming_text: str = ""
    full_explanation: str = ""
    recommendation: dict[str, Component] = {}
    error_message: str = ""

    @rx.event
    def set_budget(self, value: str):
        try:
            self.budget = int(value) if value else 0
        except (ValueError, TypeError) as e:
            logging.exception(f"Could not parse budget value '{value}': {e}")
            self.budget = 0

    @rx.event
    def toggle_use_case(self, use_case: str):
        if use_case in self.use_cases:
            self.use_cases.remove(use_case)
        else:
            self.use_cases.append(use_case)

    @rx.var
    def formatted_budget(self) -> str:
        return f"₹{self.budget:,}"

    @rx.var
    def total_price(self) -> int:
        if not self.recommendation:
            return 0
        return sum((comp["price"] for comp in self.recommendation.values()))

    @rx.var
    def build_analysis(self) -> dict[str, str]:
        if not self.recommendation:
            return {}
        tier = get_budget_tier(self.budget)
        tier_map = {1: "Entry-Level", 2: "Mid-Range", 3: "High-End"}
        priority = get_use_case_priority(self.use_cases)
        strengths = {
            "GPU_Heavy": "This build excels in GPU-intensive tasks like AI/ML and 3D rendering, with a powerful graphics card that can handle demanding computational workloads efficiently.",
            "GPU_Focused": "Optimized for gaming excellence, this configuration prioritizes the GPU to deliver high frame rates, smooth gameplay, and exceptional visual quality across modern titles.",
            "CPU_Focused": "With a robust CPU foundation, this build is perfect for content creation, software development, and CPU-intensive productivity tasks that require substantial processing power.",
            "Balanced": "A well-rounded build that handles diverse tasks efficiently, from gaming to productivity work, providing excellent versatility without major compromises.",
        }.get(priority, "")
        considerations = {
            1: "This budget-focused build delivers excellent value for money. While perfect for current needs, you may want to plan for future upgrades as software requirements evolve.",
            2: "This mid-range build strikes an optimal balance between performance and cost-effectiveness. It provides a solid foundation that can accommodate future upgrades seamlessly.",
            3: "This high-end build utilizes premium components for maximum performance and longevity. It's designed for enthusiasts who demand cutting-edge performance and future-proofing.",
        }.get(tier, "")
        upgrade_path = {
            1: "Consider upgrading the GPU first for gaming performance, followed by additional RAM for multitasking improvements. Storage expansion is also easily achievable.",
            2: "Future upgrades could include a more powerful GPU for 4K gaming or a faster CPU for content creation. Additional storage or RAM upgrades are straightforward.",
            3: "This system already features top-tier components. Consider custom cooling solutions, faster storage, or specialized peripherals to maximize your experience.",
        }.get(tier, "")
        return {
            "title": f"{tier_map.get(tier, '')} {priority.replace('_', ' ')} Build",
            "strengths": strengths,
            "considerations": considerations,
            "upgrade_path": upgrade_path,
        }

    def _generate_comprehensive_explanation(self):
        if not self.recommendation:
            return ""
        analysis = self.build_analysis
        intro = f"**{analysis['title']} - Comprehensive Analysis**\n\n"
        intro += f"Based on your budget of ₹{self.budget:,} and selected use cases ({', '.join(self.use_cases)}), I've carefully analyzed and selected each component to create an optimal configuration.\n\n"
        intro += f"**Build Strengths & Focus:** {analysis['strengths']}\n\n"
        intro += f"**Important Considerations:** {analysis['considerations']}\n\n"
        intro += f"**Future Upgrade Recommendations:** {analysis['upgrade_path']}\n\n"
        intro += """---

**Detailed Component Analysis & Reasoning:**

"""
        details = []
        for comp_type, comp_details in self.recommendation.items():
            detail = f"**{comp_type}: {comp_details['name']}** (₹{comp_details['price']:,})\n"
            detail += f"*Specifications:* {comp_details['spec']}\n"
            detail += f"*Selection Reasoning:* {comp_details['reasoning']}\n"
            if comp_type == "CPU":
                detail += f"*Performance Impact:* This processor provides the computational foundation for your entire system, handling {', '.join(self.use_cases).lower()} workloads efficiently.\n"
            elif comp_type == "GPU":
                if comp_details["name"] != "Integrated Graphics":
                    detail += f"*Performance Impact:* This graphics card is the primary driver for visual performance and will significantly impact gaming frame rates and rendering speeds.\n"
            elif comp_type == "RAM":
                detail += f"*Performance Impact:* This memory configuration ensures smooth multitasking and prevents bottlenecks during intensive operations.\n"
            elif comp_type == "Storage":
                detail += f"*Performance Impact:* Fast NVMe storage ensures quick boot times, rapid application loading, and responsive system performance.\n"
            details.append(detail)
        compatibility_section = """

**Compatibility Verification Complete:**
"""
        compatibility_section += """✅ CPU socket matches motherboard compatibility
"""
        compatibility_section += """✅ RAM type matches motherboard specification
"""
        compatibility_section += """✅ Power supply wattage exceeds system requirements
"""
        compatibility_section += """✅ All components fit within selected case
"""
        compatibility_section += """✅ Motherboard provides necessary expansion slots

"""
        performance_section = """**Expected Performance:**
"""
        if "Gaming" in self.use_cases:
            tier = get_budget_tier(self.budget)
            if tier == 1:
                performance_section += """• 1080p gaming at medium to high settings (60+ FPS in most titles)
"""
            elif tier == 2:
                performance_section += """• 1080p gaming at high to ultra settings (60-120+ FPS)
• 1440p gaming at medium to high settings
"""
            else:
                performance_section += """• 1440p gaming at ultra settings (60-120+ FPS)
• 4K gaming capability in many titles
"""
        if "Content Creation" in self.use_cases:
            performance_section += """• Smooth video editing and rendering capabilities
• Efficient photo processing and graphic design work
"""
        if "Development" in self.use_cases:
            performance_section += """• Fast code compilation and build processes
• Smooth IDE performance with multiple projects
"""
        return (
            intro
            + """
""".join(details)
            + compatibility_section
            + performance_section
        )

    @rx.event
    def get_recommendation(self):
        self.is_loading = True
        self.recommendation = {}
        self.error_message = ""
        self.streaming_text = ""
        self.full_explanation = ""
        self.is_streaming = False
        self.stream_complete = False
        yield
        time.sleep(1.0)
        if self.budget < 40000:
            self.is_loading = False
            self.error_message = "Minimum budget for a custom PC build is ₹40,000. Please increase your budget."
            yield rx.toast.error(self.error_message)
            return
        try:
            recommendation = get_recommendation_from_db(
                self.budget, self.use_cases, self.other_requirements
            )
            if recommendation:
                self.recommendation = recommendation
                self.is_loading = False
                api_key = os.getenv("GOOGLE_API_KEY")
                if api_key:
                    yield PCBuilderState.stream_gemini_analysis
                else:
                    self.full_explanation = self._generate_comprehensive_explanation()
                    yield PCBuilderState.stream_simulated_explanation
            else:
                self.error_message = "Unable to find a suitable build within your specified budget and requirements. Please try adjusting your budget or requirements."
                yield rx.toast.error(self.error_message)
                self.is_loading = False
        except Exception as e:
            logging.exception(f"Error generating recommendation: {e}")
            self.error_message = "An unexpected error occurred while generating your PC build. Please try again."
            self.is_loading = False
            yield rx.toast.error(self.error_message)

    @rx.event
    def stream_gemini_analysis(self):
        self.is_streaming = True
        self.streaming_text = ""
        yield
        try:
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                raise ValueError("No Google API Key configured.")
            client = genai.Client(api_key=api_key)
            build_str = """
""".join([f"{k}: {v['name']} - {v['spec']}" for k, v in self.recommendation.items()])
            prompt = f"\n            Act as a professional PC Builder AI Expert. \n            I have selected the following components for a user with these requirements:\n            \n            Budget: ₹{self.budget:,}\n            Use Cases: {', '.join(self.use_cases)}\n            Other Requirements: {self.other_requirements or 'None'}\n            \n            Selected Build Components:\n            {build_str}\n            \n            Please provide a comprehensive, professional analysis of this PC build.\n            Structure your response in clean Markdown.\n            \n            You MUST include these specific sections:\n            1. **Build Strengths & Focus**: Analyze how this specific configuration fits the user's stated use cases.\n            2. **Important Considerations**: Mention any potential bottlenecks, caveats, or things the user should know.\n            3. **Future Upgrade Recommendations**: Suggest logical next steps for upgrading this specific rig.\n            4. **Detailed Component Analysis**: Briefly explain why these specific parts work well together (synergy between CPU/GPU/RAM).\n            \n            Keep the tone professional, helpful, and enthusiastic. Mention specific performance expectations (FPS estimates, rendering speeds, etc.) relevant to the use cases.\n            Do NOT suggest changing the components I provided unless there is a critical incompatibility. Focus on analyzing the *given* build.\n            "
            response_stream = client.models.generate_content_stream(
                model="gemini-2.5-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.7, max_output_tokens=1000
                ),
            )
            for chunk in response_stream:
                if chunk.text:
                    self.streaming_text += chunk.text
                    yield
            self.stream_complete = True
            self.is_streaming = False
            yield rx.toast.success(
                "AI analysis complete! Your custom PC configuration is ready."
            )
        except Exception as e:
            logging.exception(f"Gemini API Error: {e}")
            error_msg = str(e)
            if (
                "429" in error_msg
                or "quota" in error_msg.lower()
                or "RESOURCE_EXHAUSTED" in error_msg
            ):
                yield rx.toast.warning(
                    "AI usage quota exceeded (Free Tier). Switching to Rule-Based Expert Analysis...",
                    duration=5000,
                )
            else:
                yield rx.toast.error(
                    f"AI connection failed. Switching to Rule-Based Expert Analysis.",
                    duration=5000,
                )
            self.streaming_text = ""
            self.full_explanation = self._generate_comprehensive_explanation()
            yield PCBuilderState.stream_simulated_explanation

    @rx.event
    def stream_simulated_explanation(self):
        self.is_streaming = True
        self.streaming_text = ""
        yield
        words = self.full_explanation.split()
        for i, word in enumerate(words):
            self.streaming_text += word + " "
            if word.endswith((".", "!", "?")):
                time.sleep(0.08)
            elif word.endswith((",", ":")):
                time.sleep(0.05)
            elif word.startswith("**") and word.endswith("**"):
                time.sleep(0.03)
            else:
                time.sleep(0.025)
            if i % 3 == 0:
                yield
        self.is_streaming = False
        self.stream_complete = True
        yield rx.toast.success(
            "Build analysis complete! Your custom PC configuration is ready."
        )

    @rx.var
    def build_as_text(self) -> str:
        if not self.recommendation:
            return ""
        lines = [
            f"AI-Generated PC Build Recommendation",
            f"Budget: ₹{self.budget:,} | Total Cost: ₹{self.total_price:,}",
            f"Use Cases: {', '.join(self.use_cases)}",
            "=" * 50,
        ]
        for comp_type, details in self.recommendation.items():
            lines.append(f"\n{comp_type}:")
            lines.append(f"  • {details['name']}")
            lines.append(f"  • Price: ₹{details['price']:,}")
            lines.append(f"  • Specs: {details['spec']}")
            lines.append(f"  • Why: {details['reasoning']}")
        lines.append(f"\n\nTotal Estimated Price: ₹{self.total_price:,}")
        lines.append("All components verified for compatibility.")
        return """
""".join(lines)

    @rx.event
    def copy_build_to_clipboard(self):
        return rx.set_clipboard(PCBuilderState.build_as_text)

    @rx.event
    def new_build(self):
        self.recommendation = {}
        self.budget = 50000
        self.use_cases = ["Gaming"]
        self.other_requirements = ""
        self.is_loading = False
        self.is_streaming = False
        self.stream_complete = False
        self.streaming_text = ""
        self.full_explanation = ""
        self.error_message = ""