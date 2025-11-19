import reflex as rx
from app.state import PCBuilderState


def _use_case_card(use_case: dict) -> rx.Component:
    is_selected = PCBuilderState.use_cases.contains(use_case["name"])
    return rx.el.div(
        rx.el.div(
            rx.icon(
                use_case["icon"],
                size=24,
                class_name=rx.cond(
                    is_selected,
                    "text-emerald-500",
                    "text-gray-500 group-hover:text-emerald-500",
                ),
            ),
            class_name="p-3 bg-gray-100 rounded-lg",
        ),
        rx.el.p(use_case["name"], class_name="font-semibold text-sm mt-2"),
        on_click=lambda: PCBuilderState.toggle_use_case(use_case["name"]),
        class_name=rx.cond(
            is_selected,
            "flex flex-col items-center justify-center p-4 rounded-xl border-2 border-emerald-500 bg-emerald-50 cursor-pointer transition-all duration-200 shadow-sm",
            "flex flex-col items-center justify-center p-4 rounded-xl border border-gray-200 bg-white hover:border-emerald-400 hover:bg-emerald-50/50 cursor-pointer transition-all duration-200 group",
        ),
    )


def builder_form() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "1. What's your budget?",
            class_name="text-xl font-semibold text-gray-800 mb-4",
        ),
        rx.el.div(
            rx.el.span(
                "₹", class_name="absolute left-4 top-1/2 -translate-y-1/2 text-gray-500"
            ),
            rx.el.input(
                placeholder="e.g., 80000",
                type="number",
                default_value=PCBuilderState.budget.to_string(),
                on_change=PCBuilderState.set_budget.debounce(300),
                class_name="w-full pl-8 pr-4 py-3 text-lg rounded-xl border border-gray-300 focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-colors duration-200",
            ),
            class_name="relative mb-8",
        ),
        rx.el.h2(
            "2. How will you use this PC?",
            class_name="text-xl font-semibold text-gray-800 mb-4",
        ),
        rx.el.div(
            rx.foreach(PCBuilderState.all_use_cases, _use_case_card),
            class_name="grid grid-cols-2 md:grid-cols-3 gap-4 mb-8",
        ),
        rx.el.h2(
            "3. Any other requirements?",
            class_name="text-xl font-semibold text-gray-800 mb-4",
        ),
        rx.el.textarea(
            placeholder="e.g., White themed build, liquid cooling, specific brands like Intel/NVIDIA...",
            on_change=PCBuilderState.set_other_requirements.debounce(300),
            class_name="w-full p-4 rounded-xl border border-gray-300 focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-colors duration-200 min-h-[120px]",
        ),
        class_name="w-full max-w-2xl",
    )