import flet
from flet import Page, Text

def main(page):
    page.add(Text(f"Intial route: {page.route}"))
    def route_change(route):
        page.add(Text(f"new route: {route}"))
    page.on_route_change = route_change
    page.update()
flet.app(target=main, view=flet.WEB_BROWSER)