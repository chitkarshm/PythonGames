import random
def make_PIN():
      PIN = ""
      while len(PIN) < 4:
        digit = random.randint(0, 9)
        PIN = PIN + str(digit)
      print(f"Your PIN is {PIN} ")

def change_and_repeat():
    changePIN=input("Do you want to change your PIN?")
    while changePIN != "no":
        make_PIN()
        changePIN=input("Do you want to change your PIN?")
        if changePIN == "no":
            print("OK, bye!")
            break
make_PIN()
change_and_repeat()