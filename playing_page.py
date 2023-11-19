from designer import *
from dataclasses import dataclass
from random import randint


@dataclass
class Button:
    background: DesignerObject
    border: DesignerObject
    label: DesignerObject

def make_button(message: str, x: int, y: int) -> Button:
    horizontal_padding = 4
    vertical_padding = 2
    label = text("black", message, 20, x, y, layer='top')
    return Button(rectangle("cyan", label.width + horizontal_padding, label.height + vertical_padding, x, y),
                  rectangle("black", label.width + horizontal_padding, label.height + vertical_padding, x, y, 1),
                  label)

@dataclass
class BlankScreen:
    button_a: Button
    button_b: Button
    button_c: Button
    button_d: Button


def create_title_text(message: str, x: int, y: int) -> DesignerObject:
    title = text("black", message, 20, x, y, layer='top')

def create_blank_screen() -> BlankScreen:
    button_width = 150
    button_height = 50
    button_spacing = 20

    total_button_width = 4 * button_width + 3 * button_spacing
    x_start = (get_width() - total_button_width) / 2 + 76
    y_position = get_height() - 100
    return BlankScreen(
        make_button("Random Note", x_start, y_position),
        make_button("Random Note", x_start + button_width + button_spacing, y_position),
        make_button("Random Note", x_start + 2 * (button_width + button_spacing), y_position),
        make_button("Random Note", x_start + 3 * (button_width + button_spacing), y_position),


    )

def handle_blank_screen_buttons(world: BlankScreen):
    if colliding_with_mouse(world.button_a.background):
        print("Button A clicked!")
    elif colliding_with_mouse(world.button_b.background):
        print("Button B clicked!")
    elif colliding_with_mouse(world.button_c.background):
        print("Button C clicked!")
    elif colliding_with_mouse(world.button_d.background):
        print("Button D clicked!")

def draw_blank_screen(screen: BlankScreen):
    return (
        draw(screen.title),
        draw(screen.button_a.background),
        draw(screen.button_a.border),
        draw(screen.button_b.background),
        draw(screen.button_b.border),
        draw(screen.button_b.label),
        draw(screen.button_c.background),
        draw(screen.button_c.border),
        draw(screen.button_c.label),
        draw(screen.button_d.background),
        draw(screen.button_d.border),
        draw(screen.button_d.label))

# background_color = rectangle("pink", get_width(), get_height(), 0, 0)
# draw(background_color)
when('starting: blank screen', create_blank_screen)
when('clicking: blank screen', handle_blank_screen_buttons)
draw('blank_screen', draw_blank_screen)
debug(scene='blank_screen')
