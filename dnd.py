import flet
from flet import Container, Draggable, DragTarget, Page,Row,Text,alignment,border, colors

def main(page):
    page.title = "Drag and Drop demo"

    def drag_accept(e):
        src = page.get_control(e.data)
        src.content.content.value = "0"
        src.group = ""
        e.control.content.content.value = "1"
        e.control.content.border = None
        page.update()

    def drag_will_accept(e):
        e.control.content.border = border.all(2,colors.BLACK45 if e.data == "true" else colors.RED)
        e.control.update()

    def drag_leave(e):
        e.control.content.border = None
        e.control.update()
    page.add(
        Row(
            [
                Draggable(
                    group="number",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.CYAN_200,
                        border_radius=5,
                        content=Text("1", size=20),
                        alignment=alignment.center,
                    ),
                    content_when_dragging=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.BLUE_GREY_200,
                        border_radius=5,
                    ),
                    content_feedback=Text("1"),
                ),
                Container(width=100),
                DragTarget(
                    group="number",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.PINK_200,
                        border_radius=5,
                        content=Text("0", size=20),
                        alignment=alignment.center,
                    ),
                    on_accept=drag_accept,
                    on_will_accept=drag_will_accept,
                    on_leave=drag_leave,
                ),
            ]
        )
    )
flet.app(target = main)