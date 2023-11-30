# imports
from designer import *
from dataclasses import dataclass
from random import randint

@dataclass
class QuizScreen:
    test: DesignerObject
    questions: DesignerObject[]
    correct_Answer: str

@dataclass
class Quiz_Question:
    image: DesignerObject
    answer: str

def create_title_text(message: str, x: int, y: int) -> DesignerObject:
    title = text("black", message, 20, x, y, layer='top')
    return title

def create_quiz_screen() -> QuizScreen:
    # Create list of questions
    q1 = Quiz_Question(image("URL", x, y), "A")
    q2 = Quiz_Question()
    # List of question
    list = [q1, q2]
    return QuizScreen(create_title_text("TESTER", 200, 200), list, None)
def choose_question(quiz:QuizScreen):
    """"use rand to choose a question"""
    # remember to update corect ansewwer

def handle_user_input(quiz: QuizScreen, keys:str):
    user_input = keys
    print(user_input)
    if (user_input == 'A' or user_input == 'a'):
        print("chosen A")
        if(quiz.correct_Answer == A):
            # iterating score
    elif (user_input == 'B' or user_input == 'b'):
        print("chosen B")
    elif (user_input == 'A'):
        print("chosen A")
    elif (user_input == 'A'):
        print("chosen A")
    else:
        print("not valid input ", user_input)
        # auto incorrrect
    # Choose next question]
    choose_question(quiz)

# background_color = rectangle("pink", get_width(), get_height(), 0, 0)
# draw(background_color)
when('starting', create_quiz_screen)
when('typing', handle_user_input)
start()
#debug(scene='quiz screen')