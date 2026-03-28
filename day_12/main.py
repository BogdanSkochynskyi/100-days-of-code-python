import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
level = input("What's the level hard or easy? ")

if level == "hard":
    attempts = 5
else:
    attempts = 10
print(f"You have {attempts} attempts left")

answer = random.randint(1, 100)
print(answer)
while attempts > 0:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == answer:
        print("Congratulations! You guessed the number correctly!")
        break
    elif guess > answer:
        print("You guessed too high!")
        attempts -= 1
    elif guess < answer:
        print("You guessed too low!")
        attempts -= 1
    if attempts == 0:
        print(f"You lose! The number was {answer}")
        break
    else:
        print(f"Attempts left {attempts}")