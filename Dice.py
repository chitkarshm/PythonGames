import random
while True:
      roll = input("do you want to roll a die?")
      if roll == "yes" or roll == "y":
            dice = random.randint(1, 6)
            print("You rolled a " + str(dice) + "!")
      else:
            break