def add(x,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4):")
                   
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.Bye!")
            break

        if choice == '1':
            print(add(num1, num2))

        elif choice == '2':
            print(subtract(num1, num2))

        elif choice == '3':
            print(multiply(num1, num2))

        elif choice == '4':
            while num2 == 0:
                print(f"You cannot divide {num1} by 0.")
                num2 = float(input("Enter second number: "))
            print(divide(num1, num2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          exit()
        elif next_calculation == "yes":
            continue
        else :        
            print("Invalid Input.Bye!")
            exit()

    else:
        print("Invalid Input.Bye!")
        break