import random

num_of_die = input("do you want to roll 1 dice or 2?")
if num_of_die == "1":
    while True:
        dice = random.randint(1, 6)
        print(f"You rolled a {dice}!")
        redo = input("do you want to continue?")
        if redo == "yes" or redo == "y":
            continue
        else:
            print("OK, bye!")
            break
elif num_of_die == "2":
    while True:
        dicea = random.randint(1, 6)
        diceb = random.randint(1, 6)
        total = dicea + diceb
        print(f"You rolled a {total}!")
        redo = input("do you want to continue?")
        if redo == "yes" or redo == "y":
            continue
        else:
            print("OK, bye!")
            break
else:
    print("Please enter only 1 or 2.Bye!")
