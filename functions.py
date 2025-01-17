#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random


print("I'm thinking of a number between 1 and 100. ")

random_number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard'. ").lower()

LIVES = 0


if difficulty == "easy":
    LIVES = 10
    print(f"You have 10 attempts remaining to guess the number.")
else:
    LIVES = 5
    print(f"You have 5 attempts remaining to guess the number.")

guess = int(input("Make a guess: "))



def check_answer(number):
    global LIVES

    if guess > random_number:
        print("Too high.")
        print("Guess again. ")
        LIVES -= 1
        print(f"You have {LIVES} attempts remaining to guess the number. ")

    elif guess < random_number:
        print("Too low.")
        print("Guess again. ")
        LIVES -= 1
        print(f"You have {LIVES} attempts remaining to guess the number. ")

    elif guess == random_number:
        print(f"You got it! The answer was {random_number}")


check_answer(guess)
while LIVES != 0 and guess != random_number:
    new_guess = int(input("Make a guess: "))
    guess = new_guess
    check_answer(guess)














