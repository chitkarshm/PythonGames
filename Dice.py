import random


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
    print(f"You rolled a total of {sum}!")


def get_num_of_die():
    num_of_die = input("How many dice do you want to roll?")
    if not num_of_die.isdigit():
        print("Enter a number only.")
        return -1
    num_of_die = int(num_of_die)
    return num_of_die


while True:
    num_of_die = get_num_of_die()
    if num_of_die < 0:
        break
    roll_dice(num_of_die)
    if not ask_continue():
        break
