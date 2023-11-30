from designer import *
import score_report
def user_input(keys: str):
    user_input = keys.capitalize()
    if(user_input == 'A'):
        print("chosen A")
    elif (user_input == 'B'):
        print("chosen B")
    elif (user_input == 'A'):
        print("chosen A")
    elif (user_input == 'A'):
        print("chosen A")
    else:
        print("not valid input ", user_input)


when('typing', user_input)
