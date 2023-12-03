# imports
from designer import *
from dataclasses import dataclass
from random import *
#sets black and white musical note border
set_window_image(
    "https://media.istockphoto.com/id/1306901365/vector/frame-made-of-monochrome-musical-note-illustrations.jpg?s=612x612&w=0&k=20&c=bQcBT76sD13_LMXdQMNe7e1FEwy4YE2PZ6aE69fkVrc=")

# image for a in the treble clef
a_note = "https://www.musictheoryacademy.com/wp-content/uploads/2020/06/Treble-Clef-Notes-Quiz-A.jpg"
# image for b in the treble clef
b_note = "https://www.musictheoryacademy.com/wp-content/uploads/2020/06/Treble-Clef-Notes-Quiz-B.jpg"
# image for c in the treble clef
c_note = "https://assets.tonegym.co/posts/QX41D6.jpeg"
# image for d in the treble clef
d_note = "https://www.musictheoryacademy.com/wp-content/uploads/2020/06/Treble-Clef-Notes-Quiz-D.jpg"
# image for e in the treble clef
e_note = "https://www.musictheoryacademy.com/wp-content/uploads/2020/06/Treble-Clef-Notes-Quiz-low-E.jpg"
# image for f in the treble clef
f_note = "https://www.musictheoryacademy.com/wp-content/uploads/2020/06/Treble-Clef-Notes-Quiz-low-F.jpg"
# image for g in the treble clef
g_note = "https://www.musictheoryacademy.com/wp-content/uploads/2020/06/Treble-Clef-Notes-Quiz-G.jpg"

notes_images = [a_note, b_note, c_note,d_note,e_note,f_note,g_note]
notes = ['a','b','c','d','e','f','g']
@dataclass
class QuizScreen:
    #creates the dataclass for the entire screen
    title: DesignerObject
    current_question: DesignerObject
    correct_answer: str
    score: int
    instructions: DesignerObject
    instructions2: DesignerObject
    instructions3: DesignerObject
    score_counter: DesignerObject
    correct_message: DesignerObject
    mode: DesignerObject
    hard_mode_instructions: DesignerObject
@dataclass
class Quiz_Question:
    #creates the dataclass for the quiz questions
    image: DesignerObject
    answer: str

def create_title_text(message: str, x: int, y: int) -> DesignerObject:
    '''formats text into the title form'''
    title = text("black", message, 40, x, y)
    title.layer = 'top'
    return title

def create_question(question_number:int) -> Quiz_Question:
    '''creates quiz questions based on the lists made of notes/possible questions'''
    return Quiz_Question(image(notes_images[question_number],400,330),notes[question_number])

def create_quiz_screen() -> QuizScreen:
    '''creates the starting quiz screen before any updates'''
    random_element = randint(-1,len(notes)-1)
    initial_question = create_question(random_element)
    set_scale(initial_question.image,0.6)
    instructions1 = text("black", "For this game, you will be tested on how well you know your scales!",
                         20, 400, 150)
    instructions1.layer = "top"
    instructions2 = text("black", "You'll be shown different musical notes/key signatures.",
                         20, 400, 175)
    instructions2.layer = "top"
    instructions3 = text("black",
                         "Choose which note the image represents and increase your score! Reach 10 for hard mode and 50 for a surprise.",
                         15, 400,200)
    instructions3.layer = "top"
    easy_mode = text("black","Easy Mode",30,400,470)
    easy_mode.layer = "top"
    hard_mode_instructions = text("black","",18,400,225)
    hard_mode_instructions.layer = "top"
    correct_message = text("black","",25,400,435)
    correct_message.layer = "top"
    return QuizScreen(create_title_text("Musical Madness", 400, 100), initial_question.image,
                      initial_question.answer, 0, instructions1, instructions2, instructions3,
                      text("black","0",30,400,500), correct_message,
                      easy_mode,hard_mode_instructions)

def choose_question(quiz:QuizScreen):
    '''randomizes a new question to display and gets rid of the old
    one once it has been answered accurately so that there aren't multiple questions
    on the screen at once'''
    random_element = randint(-1, len(notes) - 1)
    new_question = create_question(random_element)
    destroy(quiz.current_question)
    quiz.correct_message.text = ''
    quiz.current_question = new_question.image
    quiz.correct_answer = new_question.answer
    set_scale(quiz.current_question,0.6)
def handle_user_input(quiz: QuizScreen, keys:str):
    '''accounts for the user input to see if the user got the answer
    correct and responds accordingly'''
    user_input = keys
    print(user_input)
    if user_input == quiz.correct_answer:
        quiz.score += 1
        choose_question(quiz)
    else:
        quiz.score -= 1
        quiz.correct_message.color = 'red'
        quiz.correct_message.text = 'Incorrect!'

def update_score(quiz):
    '''updates the score counter onscreen as the player plays'''
    quiz.score_counter.text = "Score: " + str(quiz.score)

def game_hard_mode(quiz:QuizScreen):
    '''updates the screen and adds more possible questions and answers to the
    earlier lists if the player's score is high enough to reach hard mode'''
    if quiz.score > 10:
        quiz.mode.text = "Hard Mode!"
        quiz.instructions3.text = (
            "Choose which musical concept the image represents and increase your score! Reach 50 for a surprise.")
        quiz.hard_mode_instructions.text = "For non-note-name questions, type the first letter of the represented concept."
        notes_images.append(
            "https://www.musictheoryacademy.com/wp-content/uploads/2020/06/Treble-Clef-Symbol.jpg") #treble clef
        notes_images.append(
            "https://t4.ftcdn.net/jpg/02/88/35/43/360_F_288354347_pPVuNd39jxjf4mQUOwfNneqKZuE1r1KW.jpg") #quarter note
        notes_images.append(
            "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Sixteenth_note_run.svg/220px-Sixteenth_note_run.svg.png") #sixteenth note
        notes_images.append(
            "https://static.thenounproject.com/png/98895-200.png") #half note
        notes_images.append(
            "https://upload.wikimedia.org/wikipedia/commons/4/4a/One_single_whole_note.png") #whole note
        notes_images.append(
            "https://hellomusictheory.com/wp-content/uploads/2019/02/7.6-1024x173.png") #rests
        notes.append("t") #t for treble clef
        notes.append("q") #q for quarter note
        notes.append("s") #s for sixteenth note
        notes.append("h") #h for half note
        notes.append("w") #w for whole note
        notes.append("r") #r for rests

def special_surprise(quiz: QuizScreen):
    '''updates the screen and background if the player's score is high enough
    to reach the 'musical master' qualification and earn the special surprise'''
    if quiz.score > 50:
        set_window_image(
            "https://media.istockphoto.com/id/1385311380/vector/illustration-frame-of-simple-colorful-musical-notes.jpg?s=612x612&w=0&k=20&c=JPXuGinRRjQNj6H5Kb_tQdzbwurMvRmTRiyW5a8UFv4=")
        quiz.title.color = "darkgreen"
        quiz.instructions.color = "lightskyblue"
        quiz.instructions2.color = "darkseagreen"
        quiz.instructions3.color = "lightseagreen"
        quiz.instructions3.text = "Congratulations on being a music master! Keep playing to ensure your skills stay sharp."
        quiz.mode.text = "Musical Master!"
        quiz.mode.color = "darkgreen"
        quiz.score_counter.color = "darkgreen"

#when statements to start the game and have it updating during gameplay
when('starting', create_quiz_screen)
when('typing', handle_user_input)
when('updating',update_score)
when('updating',game_hard_mode)
when('updating',special_surprise)
start()


