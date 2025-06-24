import random
import sys


def ask_continue():
    redo = input("Do you want to continue?")
    if redo == "yes" or redo == "y":
        return True
    else:
        print("OK, bye!")
        return False


def roll_dice(num_of_die):
    sum = 0
    for _ in range(0, num_of_die):
        dice = random.randint(1, 6)
        sum = dice + sum
    print(f"You rolled a {sum}!")


num_of_die = input("Do you want to roll 1 dice or 2?")
if not num_of_die.isdigit():
    print("Enter a number only.")
    sys.exit()

num_of_die = int(num_of_die)
if num_of_die == 1:
    while True:
        roll_dice(num_of_die)
        if not ask_continue():
            break
elif num_of_die == 2:
    while True:
        roll_dice(num_of_die)
        if not ask_continue():
            break
else:
    print("Enter a number only: 1 or 2")
