import flet
from flet import Container, ElevatedButton, Page, animation
from flet.transform import Scale

def main(page):
    c = Container(width=150,height=150,bgcolor="blue",border_radius=10,animate_opacity=300)
    def animate_opacity(e):
        c.opacity = 0 if c.opacity == 1 else 1
        c.update()
    d = Container(width=100,height=100,bgcolor="blue",border_radius=5,scale=Scale(scale=1),animate_scale=animation.Animation(600,"bounceOut"))
    def animate(e):
        d.scale = 2 if d.scale == 1 else 1
        d.update()

    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.spacing = 30
    page.add(c, ElevatedButton("Animate opacity",on_click=animate_opacity))
    page.add(d, ElevatedButton("Animate scale",on_click=animate))

flet.app(target = main, view = flet.WEB_BROWSER)