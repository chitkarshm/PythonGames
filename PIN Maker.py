import random
pin=""
while len(pin) < 4:
      digit = random.randint(0,9)
      pin = pin + str(digit)
print("Your PIN is " + pin )