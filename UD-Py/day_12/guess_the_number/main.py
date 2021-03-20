# Include an ASCII art logo.
import random
from art import logo
print(logo)

# Allow the player to submit a guess for a number between 1 and 100.
starting_message = "Welcome to the Number Guessing Game!"
print("Im thinking of a number between 1 and 100")

right_number = random.randint(1, 100)
# print(f"Psssst the answer is {right_number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "hard":
    lives = 5
    print(f"You have {lives} turns to guess the number\n")
else:
    lives = 10
    print(f"You have {lives} turns to guess the number\n")

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
user_guess = ""
while user_guess != right_number:
    user_guess = int(input("Make a guess: "))
    if user_guess > right_number:
        lives -= 1
        print("To High.")
        print("Guess again.")
        print(f"You have {lives} attempts left.\n")
    if user_guess < right_number:
        lives -= 1
        print("To low.")
        print("Guess again.")
        print(f"You have {lives} attempts left.\n")
    if lives == 0:
        print("You ran out of lives! Game Over.")

print(f"You got it! the answer was {right_number}.")
