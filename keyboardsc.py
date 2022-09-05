import flet
from flet import KeyboardEvent, Page, Text

def main(page):
    def on_kybrd(e: KeyboardEvent):
        page.add(
            Text(f"Key: {e.key}, shift: {e.shift}, control: {e.ctrl}, alt: {e.alt}, meta: {e.meta}")
        )
    page.on_keyboard_event = on_kybrd
    page.add(
        Text("Press any key with a combo of CTRL, ALT, SHIFT and META....")
    )

flet.app(target = main)