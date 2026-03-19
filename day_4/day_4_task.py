import random
import my_graphics

choices = [my_graphics.rock, my_graphics.paper, my_graphics.scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.")
choice = int(input())
comp_choice = random.randint(0,2)

if choice > len(choices) - 1:
    print("You lose!")
else:
    print(choices[choice])
    print("Computer chose\n" + choices[comp_choice])
    if choice == comp_choice:
        print("Draw!")
    elif choice == 0 and comp_choice == 1:
        print("You Lose!")
    elif choice == 1 and comp_choice == 2:
        print("You Lose!")
    elif choice == 2 and comp_choice == 0:
        print("You Lose!")
    else:
        print("You Win!")
