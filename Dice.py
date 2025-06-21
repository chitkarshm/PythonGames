import random


def ask_continue():
    redo = input("Do you want to continue?")
    if redo == "yes" or redo == "y":
        return True
    else:
        print("OK, bye!")
        return False


num_of_die = input("Do you want to roll 1 dice or 2?")
if num_of_die == "1":
    while True:
        dice = random.randint(1, 6)
        print(f"You rolled a {dice}!")
        if not ask_continue():
            break
elif num_of_die == "2":
    while True:
        dicea = random.randint(1, 6)
        diceb = random.randint(1, 6)
        total = dicea + diceb
        print(f"You rolled a {total}!")
        if not ask_continue():
            break
else:
    print("Please enter only 1 or 2.Bye!")
