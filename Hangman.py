import time
import random


def random_string():
    return random.choices(["frog", "baboon", "cookies", "cake", "basketball", "yay","banana"])[0]


name = input("What is your name?")
print(f"Hello {name}!Let's play Hangman!")
time.sleep(3)
print("Start guessing...")
time.sleep(0.5)
word = random_string()
guesses = ""
turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("YAY!You won!")
        break
    guess = input("Guess a character:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong guess")
        print(f"You have {turns} more guesses remaining")
        if turns == 0:
            print(f"AWW MAN!You lost!The word was {word}")
print("=======GAME OVER=======")
