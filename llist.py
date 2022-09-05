from typing import Container
import flet
from flet import Page, Text, ListView, GridView, Row, alignment,border,border_radius,colors, Container

def main(page):
    #for i in range(50):
    #    page.controls.append(Text(f"Line: {i}"))
    #page.scroll = "always"
    #page.update()

    #lv = ListView(expand = True, spacing = 10)
    #for i in range(50):
    #    lv.controls.append(Text(f"ListView: {i}"))
    #page.add(lv)
    r = Row(wrap = True, scroll = "always", expand = True)
    page.add(r)
    for i in range(100):
        r.controls.append(
            Container(Text(f"Item: {i}"),
            width = 100,
            height=100,
            alignment=alignment.center,
            bgcolor=colors.AMBER_100,
            border=border.all(1,colors.AMBER_400),
            border_radius=border_radius.all(5))
        )
    page.update()
flet.app(target = main, view = flet.WEB_BROWSER)