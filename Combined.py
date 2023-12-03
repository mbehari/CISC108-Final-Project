# imports
from designer import *
from dataclasses import dataclass
from random import *
# image for a in the treble clef
a_note = "https://www.musictheoryacademy.com/wp-content/uploads/2020/06/Treble-Clef-Notes-Quiz-A.jpg"
# image for b in the treble clef
b_note = "https://www.musictheoryacademy.com/wp-content/uploads/2020/06/Treble-Clef-Notes-Quiz-B.jpg"
# image for c in the treble clef
c_note = "https://assets.tonegym.co/posts/QX41D6.jpeg"
# image for d in the treble clef
d_note = "https://media.cheggcdn.com/media/67c/67c32be9-b5be-42ce-b54d-d6ab001d4ea4/image?height=160"
# image for e in the treble clef
e_note = "https://www.musictheoryacademy.com/wp-content/uploads/2020/06/Treble-Clef-Notes-Quiz-low-E.jpg"
# image for f in the treble clef
f_note = "https://www.musictheoryacademy.com/wp-content/uploads/2020/06/Treble-Clef-Notes-Quiz-low-F.jpg"
# image for g in the treble clef
g_note = "https://www.musictheoryacademy.com/wp-content/uploads/2020/06/Treble-Clef-Notes-Quiz-G.jpg"


@dataclass
class QuizScreen:
    text: DesignerObject
    current_question: DesignerObject
    correct_answer: str
    score: int
    #list_of_questions: list[DesignerObject]

@dataclass
class Quiz_Question:
    image: DesignerObject
    answer: str

def create_title_text(message: str, x: int, y: int) -> DesignerObject:
    title = text("black", message, 20, x, y)
    return title

qA = Quiz_Question(image(a_note, 200, 350), "a")
qB = Quiz_Question(image(b_note, 200, 350), "b")
qC = Quiz_Question(image(c_note, 200, 350), "c")
qD = Quiz_Question(image(d_note, 200, 350), "d")
qE = Quiz_Question(image(e_note, 200, 350), "e")
qF = Quiz_Question(image(f_note, 200, 350), "f")
qG = Quiz_Question(image(g_note, 200, 350), "g")
list_of_questions = [qA, qB, qC, qD, qE, qF, qG]

def create_quiz_screen() -> QuizScreen:
    random_element = randint(-1,len(list_of_questions)-1)
    initial_question = list_of_questions[random_element]
    return QuizScreen(create_title_text("Musical Madness", 400, 200), initial_question.image, initial_question.answer, 0)

def choose_question(quiz:QuizScreen):
    random_element = randint(-1, len(list_of_questions) - 1)
    new_question = list_of_questions[random_element]
    quiz.current_question = new_question.image
    quiz.correct_answer = new_question.answer

def handle_user_input(quiz: QuizScreen, keys:str):
    user_input = keys
    print(user_input)
    if user_input == quiz.correct_answer:
        print("Chosen", quiz.correct_answer)
        quiz.score += 1
        print("Score:", quiz.score)
        #hide(quiz.current_question)
        choose_question(quiz)
        #show(quiz.current_question)
    else:
        print("Chosen", user_input, "- Incorrect")


when('starting', create_quiz_screen)
when('typing', handle_user_input)
start()
#debug(scene='quiz screen')


