import reflex as rx
from app.state import PCBuilderState
from app.components.form import builder_form
from app.components.result import result_display
from app.components.demo import demo_page


def hero_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("cpu", size=48, class_name="text-emerald-500"),
            class_name="p-4 bg-emerald-100 rounded-2xl mb-6 shadow-sm border border-emerald-200",
        ),
        rx.el.h1(
            "Build Your Dream PC with AI",
            class_name="text-4xl md:text-6xl font-bold tracking-tighter text-gray-900 mb-4 text-center font-['Lora']",
        ),
        rx.el.p(
            "Tell us your budget and needs. Our AI will craft the perfect PC configuration for you, checking compatibility and estimating prices in INR.",
            class_name="text-lg md:text-xl text-gray-600 max-w-3xl text-center mb-10",
        ),
        class_name="flex flex-col items-center justify-center pt-24 pb-16",
    )


def result_placeholder() -> rx.Component:
    return rx.el.div(
        rx.cond(
            PCBuilderState.is_loading,
            rx.el.div(
                rx.spinner(size="3", class_name="text-emerald-500"),
                rx.el.p(
                    "Analyzing requirements and crafting your build...",
                    class_name="mt-4 text-gray-600 font-medium",
                ),
                class_name="flex flex-col items-center justify-center p-12 bg-gray-50 rounded-2xl border border-dashed border-gray-300 transition-all",
            ),
            rx.cond(
                PCBuilderState.recommendation.keys().length() > 0,
                result_display(),
                rx.el.div(
                    rx.icon("search", size=32, class_name="text-gray-400 mb-4"),
                    rx.el.h3(
                        "Your AI-Generated PC Build",
                        class_name="text-lg font-semibold text-gray-700 mb-1",
                    ),
                    rx.el.p(
                        "Your configuration and build analysis will appear here.",
                        class_name="text-gray-500 text-sm",
                    ),
                    class_name="flex flex-col items-center justify-center text-center p-12 bg-gray-50 rounded-2xl border border-dashed border-gray-300 transition-all",
                ),
            ),
        ),
        class_name="w-full max-w-4xl mt-12 flex justify-center",
    )


def index() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            hero_section(),
            rx.el.div(
                builder_form(),
                rx.el.div(
                    rx.el.button(
                        rx.icon("zap", class_name="mr-2"),
                        "Generate Build",
                        on_click=PCBuilderState.get_recommendation,
                        is_loading=PCBuilderState.is_loading,
                        disabled=PCBuilderState.is_streaming,
                        class_name="w-full md:w-auto px-12 py-4 text-lg font-semibold text-white bg-emerald-600 rounded-xl hover:bg-emerald-700 transition-all duration-200 shadow-lg hover:shadow-emerald-300/40 focus:ring-4 focus:ring-emerald-300 flex items-center justify-center disabled:bg-emerald-300 disabled:cursor-not-allowed",
                    ),
                    class_name="w-full max-w-2xl flex justify-center mt-10",
                ),
                result_placeholder(),
                class_name="w-full flex flex-col items-center px-4 pb-24",
            ),
            class_name="min-h-screen bg-gray-50",
        ),
        class_name="font-['Lora']",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Lora:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")
app.add_page(demo_page, route="/demo")