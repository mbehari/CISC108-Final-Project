from designer import *
from dataclasses import dataclass
@dataclass
class World:
    title_message: DesignerObject
    correct_message: DesignerObject
    musical_notes: list[DesignerObject]
    total_score: int
    counter: DesignerObject

score_counter = text("black", "0", 30, 400, 100)
game_name = text("black","hello",30,30,30)
that_is_correct = text("black","hello",12,300,300)
photos_of_notes_list = [game_name,that_is_correct]
final_score = 2

new_screen = World(game_name,that_is_correct,photos_of_notes_list,final_score,score_counter)
# game_name is defined on title.py file
# photos_of_notes list is defined on photos_of_notes.py
# that_is_correct still needs to be defined
# final_score



def update_score(world):
    new_screen.counter.text = "Your score is " + str(new_screen.total_score)
    test_variable = True # this line was used for testing function
    #if test_variable == True: # this line was used for testing, change code later to reflect correct/incorrect
        #update_score(new_screen)

#draw(new_screen.counter)