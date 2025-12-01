import reflex as rx
from app.state import PCBuilderState


def code_evidence_section() -> rx.Component:
    code_snippet = """
# Real Gemini API call with streaming
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
response_stream = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=0.7, 
        max_output_tokens=1000
    ),
)
for chunk in response_stream:
    if chunk.text:
        self.streaming_text += chunk.text
        yield  # Updates UI in real-time
"""
    return rx.el.div(
        rx.el.h2(
            "1. Code Evidence", class_name="text-2xl font-bold text-gray-800 mb-4"
        ),
        rx.el.p(
            "The following code snippet from app/state.py handles the real-time connection to Google's Gemini API:",
            class_name="text-gray-600 mb-4",
        ),
        rx.el.pre(
            rx.el.code(code_snippet, class_name="language-python text-sm font-mono"),
            class_name="bg-gray-900 text-emerald-400 p-6 rounded-xl overflow-x-auto border border-gray-700 shadow-inner",
        ),
        class_name="bg-white p-8 rounded-2xl border border-gray-200 shadow-sm mb-8",
    )


def streaming_demo_section() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "2. Live Streaming Demo", class_name="text-2xl font-bold text-gray-800 mb-4"
        ),
        rx.el.p(
            "Click the button below to send a test request to Gemini 2.5 Flash. This proves the application is making real network calls and streaming the response token-by-token.",
            class_name="text-gray-600 mb-6",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("play", class_name="mr-2"),
                "Test Live Gemini Stream",
                on_click=PCBuilderState.start_demo_stream,
                disabled=PCBuilderState.is_demo_streaming,
                class_name="bg-emerald-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-emerald-700 transition-colors flex items-center disabled:opacity-50 disabled:cursor-not-allowed",
            ),
            class_name="mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Gemini 2.5 Flash Response:",
                    class_name="text-xs font-bold text-emerald-500 uppercase tracking-wider mb-2 block",
                ),
                rx.el.p(
                    PCBuilderState.demo_output,
                    class_name="text-gray-800 font-medium leading-relaxed min-h-[60px]",
                ),
                rx.cond(
                    PCBuilderState.is_demo_streaming,
                    rx.el.span(
                        "_",
                        class_name="inline-block w-2 h-4 bg-emerald-500 animate-pulse ml-1 align-middle",
                    ),
                    None,
                ),
                class_name="bg-emerald-50/50 border-2 border-emerald-100 rounded-xl p-6 relative",
            ),
            class_name="relative",
        ),
        class_name="bg-white p-8 rounded-2xl border border-gray-200 shadow-sm mb-8",
    )


def comparison_section() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "3. Output Comparison", class_name="text-2xl font-bold text-gray-800 mb-4"
        ),
        rx.el.p(
            "Contrast the dynamic, conversational nature of Gemini AI against the static templates of the fallback system.",
            class_name="text-gray-600 mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "🤖 AI (Gemini 2.5)",
                    class_name="text-lg font-bold text-emerald-700 mb-3 flex items-center",
                ),
                rx.el.div(
                    "Based on your budget of ₹75,000 and focus on Gaming and Content Creation, I've crafted a balanced configuration that excels in both domains. The RTX 4060 paired with Ryzen 5 5600 creates exceptional synergy for 1080p gaming while maintaining strong rendering capabilities...",
                    class_name="text-sm text-gray-700 italic leading-relaxed",
                ),
                class_name="flex-1 p-6 bg-emerald-50 rounded-xl border border-emerald-200",
            ),
            rx.el.div(
                rx.el.h3(
                    "📝 Rule-Based (Fallback)",
                    class_name="text-lg font-bold text-gray-700 mb-3 flex items-center",
                ),
                rx.el.div(
                    """**Entry-Level GPU Focused Build - Comprehensive Analysis**
Based on your budget of ₹75,000 and selected use cases (Gaming, Content Creation)...
**Build Strengths & Focus:** Optimized for gaming excellence, this configuration prioritizes the GPU to deliver high frame rates...""",
                    class_name="text-sm text-gray-600 leading-relaxed whitespace-pre-line",
                ),
                class_name="flex-1 p-6 bg-gray-50 rounded-xl border border-gray-200",
            ),
            class_name="flex flex-col md:flex-row gap-6",
        ),
        class_name="bg-white p-8 rounded-2xl border border-gray-200 shadow-sm mb-8",
    )


def verification_section() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "4. API Verification", class_name="text-2xl font-bold text-gray-800 mb-4"
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Environment Variable Status",
                    class_name="text-sm text-gray-500 mb-1",
                ),
                rx.el.div(
                    rx.el.code(
                        "GOOGLE_API_KEY",
                        class_name="text-purple-600 font-mono font-bold mr-3",
                    ),
                    rx.el.span(
                        PCBuilderState.masked_api_key,
                        class_name="font-mono text-gray-700 bg-gray-100 px-2 py-1 rounded",
                    ),
                    class_name="flex items-center",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.p("Dependencies", class_name="text-sm text-gray-500 mb-1"),
                rx.el.div(
                    rx.el.span(
                        "google-genai",
                        class_name="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm font-semibold mr-2",
                    ),
                    rx.el.span(
                        "reflex",
                        class_name="px-3 py-1 bg-gray-100 text-gray-800 rounded-full text-sm font-semibold",
                    ),
                    class_name="flex flex-wrap",
                ),
            ),
            class_name="bg-gray-50 p-6 rounded-xl border border-gray-200",
        ),
        class_name="bg-white p-8 rounded-2xl border border-gray-200 shadow-sm mb-8",
    )


def demo_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Teacher Demonstration Guide",
                    class_name="text-3xl md:text-4xl font-bold text-gray-900 mb-2 font-['Lora']",
                ),
                rx.el.p(
                    "Use this page to verify the integration of Gemini AI in the PC Builder application.",
                    class_name="text-lg text-gray-600",
                ),
                class_name="mb-8 text-center",
            ),
            code_evidence_section(),
            streaming_demo_section(),
            comparison_section(),
            verification_section(),
            rx.el.div(
                rx.el.a(
                    rx.el.button(
                        rx.icon("file-down", class_name="mr-2"),
                        "Download Full Report (PDF/MD)",
                        class_name="bg-gray-900 text-white px-8 py-4 rounded-xl font-semibold hover:bg-gray-800 transition-all shadow-lg hover:shadow-xl flex items-center text-lg",
                    ),
                    href="/teacher_demo_guide.md",
                    download="Teacher_Demonstration_Guide.md",
                    class_name="no-underline",
                ),
                class_name="flex justify-center pb-12",
            ),
            class_name="max-w-4xl mx-auto px-4 py-12",
        ),
        class_name="min-h-screen bg-gray-50 font-['Inter']",
    )