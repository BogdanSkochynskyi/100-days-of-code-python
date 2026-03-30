import random

from art import *
from game_data import *

#Get random accs from game data
celebrities = []

def game():
    score = 0
    is_game_over = False
    celebrity1 = get_next_celebrity(celebrities)
    while not is_game_over:
        # Print logo
        print(logo)
        update_celebrity(celebrities, celebrity1)
        celebrity2 = get_next_celebrity(celebrities)
        # If game data size become 0 - print game over and user score
        if celebrity2 == -1:
            game_over(True, score)
            is_game_over = True
        else:
            update_celebrity(celebrities, celebrity2)
            print_celebrities(celebrity1, celebrity2)
            user_select = input("Who have more subscribers in the instagram? a or b?")
            result = check_answer(celebrity1['follower_count'], celebrity2['follower_count'], user_select)

            # If user correct - then acc1 = acc2 and randomly choose next acc2, increase score
            if result:
                celebrity1 = celebrity2
                score += 1
                print_score(score)
            # If user wrong - print game over and score
            else:
                game_over(False, score)
                is_game_over = True


def update_score(local_score):
    local_score += 1
    return local_score

def get_next_celebrity(local_celebrities):
    celebrity = random.choice(data)
    if len(celebrities) < len(data):
        while celebrity in local_celebrities:
            celebrity = random.choice(data)
    else:
        return -1
    return celebrity

def update_celebrity(local_celebrities, celebrity):
    local_celebrities.append(celebrity)
    return local_celebrities

#Print score, acc1, vs, acc 2 and ask who is winner
def print_score(score):
    print(f"User score is {score}! Good luck next!")

def print_celebrities(celebrity1, celebrity2):
    print_celebrity(celebrity1)
    print(vs)
    print_celebrity(celebrity2)

def print_celebrity(celebrity):
    print(f"{celebrity['name']} who is {celebrity['description']} from {celebrity['country']} {celebrity['follower_count']}")

#Compare subscribers and user answer
def check_answer(celebrity1_subscribers, celebrity2_subscribers, user_select):
    if user_select.lower() == "a" and celebrity1_subscribers > celebrity2_subscribers:
        return True
    elif user_select.lower() == "b" and celebrity2_subscribers > celebrity1_subscribers:
        return True
    else:
        return False

def game_over(is_win, score):
    if is_win:
        print(f"You win! Your score is {score}!")
    else:
        print(f"You lose! Your score is {score}!")

game()