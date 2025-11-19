import reflex as rx
from app.state import PCBuilderState


def component_card(component: list[str]) -> rx.Component:
    comp_type = component[0]
    comp_details = component[1]
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(comp_type, class_name="text-sm font-semibold text-gray-500"),
                rx.el.p(
                    f"₹{comp_details['price']:,}",
                    class_name="font-bold text-lg text-emerald-600",
                ),
                class_name="flex justify-between items-start mb-2",
            ),
            rx.el.p(
                comp_details["name"],
                class_name="font-semibold text-gray-800 leading-tight mb-2",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("lightbulb", size=14, class_name="mr-1.5 text-yellow-500"),
                    rx.el.p(
                        comp_details["reasoning"],
                        class_name="text-xs text-gray-600 font-medium",
                    ),
                    class_name="flex items-start",
                ),
                class_name="p-2 bg-yellow-50/70 rounded-md border border-yellow-200/50",
            ),
            class_name="flex-1",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("info", size=14, class_name="mr-1.5 text-gray-400"),
                rx.el.p(comp_details["spec"], class_name="text-xs text-gray-600"),
                class_name="flex items-center mt-3 pt-3 border-t border-gray-100",
            )
        ),
        class_name="p-4 bg-white rounded-xl border border-gray-200 hover:border-emerald-400 transition-colors duration-200 flex flex-col justify-between",
    )


def streaming_analysis() -> rx.Component:
    return rx.el.div(
        rx.markdown(
            PCBuilderState.streaming_text,
            class_name="prose prose-sm max-w-none text-gray-700 leading-relaxed",
            custom_attrs={
                "components": {
                    "p": {"class_name": "mb-3"},
                    "h2": {"class_name": "text-xl font-bold mt-6 mb-2 text-gray-800"},
                    "strong": {"class_name": "font-semibold text-gray-900"},
                }
            },
        ),
        rx.cond(
            PCBuilderState.is_streaming,
            rx.el.span("_", class_name="animate-pulse"),
            None,
        ),
        class_name="p-6 bg-white rounded-xl border border-gray-200 min-h-[200px]",
    )


def result_display() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Your AI-Generated Build Analysis",
            class_name="text-3xl font-bold text-gray-800 mb-6 font-['Lora'] text-center",
        ),
        rx.el.div(
            streaming_analysis(),
            rx.cond(
                PCBuilderState.stream_complete,
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.p(
                                "Total Estimated Price",
                                class_name="text-lg font-semibold text-gray-800",
                            ),
                            rx.el.p(
                                f"₹{PCBuilderState.total_price:,}",
                                class_name="text-2xl font-bold text-emerald-600",
                            ),
                            class_name="flex justify-between items-center p-4 bg-emerald-50 rounded-t-xl border-b border-emerald-200",
                        ),
                        rx.el.div(
                            rx.el.p("Compatibility Check", class_name="font-semibold"),
                            rx.el.div(
                                rx.icon(
                                    "shield-check",
                                    size=20,
                                    class_name="text-emerald-600",
                                ),
                                rx.el.p(
                                    "All parts are compatible",
                                    class_name="text-emerald-700 font-medium",
                                ),
                                class_name="flex items-center gap-2 px-3 py-1 bg-emerald-100 rounded-full text-sm",
                            ),
                            class_name="flex justify-between items-center p-4 bg-white rounded-b-xl border-t border-gray-200",
                        ),
                        class_name="mb-6 shadow-sm",
                    ),
                    rx.el.h3(
                        "Component Breakdown",
                        class_name="text-2xl font-bold text-gray-800 mb-4 font-['Lora']",
                    ),
                    rx.el.div(
                        rx.foreach(
                            PCBuilderState.recommendation.items(), component_card
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
                    ),
                    rx.el.div(
                        rx.el.button(
                            rx.icon("copy", class_name="mr-2"),
                            "Copy Build",
                            on_click=PCBuilderState.copy_build_to_clipboard,
                            class_name="flex items-center justify-center px-4 py-2 bg-gray-100 text-gray-700 font-semibold rounded-lg hover:bg-gray-200 transition-all duration-200",
                        ),
                        rx.el.button(
                            rx.icon("download", class_name="mr-2"),
                            "Download .txt",
                            on_click=rx.download(
                                data=PCBuilderState.build_as_text,
                                filename="pc_build.txt",
                            ),
                            class_name="flex items-center justify-center px-4 py-2 bg-gray-100 text-gray-700 font-semibold rounded-lg hover:bg-gray-200 transition-all duration-200",
                        ),
                        rx.el.button(
                            rx.icon("refresh-cw", class_name="mr-2"),
                            "New Build",
                            on_click=PCBuilderState.new_build,
                            class_name="flex items-center justify-center px-4 py-2 bg-emerald-600 text-white font-semibold rounded-lg hover:bg-emerald-700 transition-all duration-200",
                        ),
                        class_name="flex flex-wrap justify-center gap-4 mt-8",
                    ),
                    class_name="w-full space-y-6 mt-8",
                ),
                None,
            ),
        ),
        class_name="w-full max-w-4xl p-6 md:p-8 bg-gray-50/50 rounded-2xl shadow-lg border border-gray-100",
    )