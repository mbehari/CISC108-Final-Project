from designer import *
from designer import *


def on_button_click():
    print("Button clicked!")


button1 = rectangle("blue", 100, 50, x=50, y=100)
button2 = rectangle("green", 100, 50, x=200, y=100)
button3 = rectangle("red", 100, 50, x=350, y=100)
button4 = rectangle("yellow", 100, 50, x=500, y=100)
draw(button1, button2, button3, button4)

when(button1, 'clicking', on_button_click)
when(button2, 'clicking', on_button_click)
when(button3, 'clicking', on_button_click)
when(button4, 'clicking', on_button_click)



