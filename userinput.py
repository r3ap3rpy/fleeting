import flet
from flet import IconButton, Page, Row, TextField, icons

def main(page: Page):
    page.tile = "Example"
    page.vertical_alignment = "center"
    txt_number = TextField(value='0', text_align ="right", width = 100)

    def minus(e):
        txt_number.value = int(txt_number.value) -1
        page.update()

    def plus(e):
        txt_number.value = int(txt_number.value) +1
        page.update()

    page.add(
        Row([
            IconButton(icons.REMOVE, on_click=minus),txt_number,
            IconButton(icons.ADD, on_click=plus),

        ],
        alignment='center',
        )
    )

flet.app(target = main)