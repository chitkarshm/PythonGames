
def ask_continue():
    redo = input("Do you want to continue?")
    if redo == "yes" or redo == "y":
        return True
    else:
        print("OK, bye!")
        exit()
while True:
      num=input("Type in a number.")
      if not num.isdigit():
            print("Enter a number only.")
            exit()

      num = int(num)
      if num == 0:
           print("This number is not even nor odd.")
      elif num % 2 == 0:
            print("This number is even.")
      else:
            print("This number is odd.")
      ask_continue()
