from dataclasses import dataclass
from designer import *
from random import *
@dataclass
class Screen:
     #maze_walls: list[DesignerObject]
     player_character: DesignerObject
     character_speed: int
     #musical_notes: list[DesignerObject]
     #score: int
     #counter: DesignerObject
CHARACTER_SPEED = 3
def create_character() -> DesignerObject:
    character = emoji("ghost", 600, 0)
    character.y = get_height() * (1/3)
    character.flip_x = True
    return character
def move_character(screen:Screen):
    screen.player_character.x += screen.character_speed
    #screen.player_character.y += screen.character_speed

def head_left(screen: Screen):
    screen.character_speed = -CHARACTER_SPEED
    screen.player_character.flip_x = False
def head_right(screen: Screen):
    screen.character_speed = CHARACTER_SPEED
    screen.player_character.flip_x = True
def head_down(screen:Screen):
    screen.player_character_speed = CHARACTER_SPEED
    screen.player_character.flip_y = False
    glide_down(screen.player_character, 80)
def head_up(screen:Screen):
    screen.player_character_speed = CHARACTER_SPEED
    screen.player_character.flip_y = False
    glide_up(screen.player_character, 80)


def bounce_character(screen: Screen):
    if screen.player_character.x > get_width():
        head_left(screen)
    elif screen.player_character.x < 0:
        head_right(screen)
    if screen.player_character.y > get_height():
        head_up(screen)
    elif screen.player_character.y < 0:
        head_down(screen)

def flip_character(screen: Screen, key: str):
    if key == "left":
        head_left(screen)
    elif key == "right":
        head_right(screen)
    elif key == "down":
        head_down(screen)
    elif key == "up":
        head_up(screen)

def create_screen() -> Screen:
    return Screen(create_character(), CHARACTER_SPEED)
when("starting", create_screen)
when("updating",move_character)
when("updating",bounce_character)
when("typing", flip_character)
start()