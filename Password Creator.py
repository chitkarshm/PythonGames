password_pone = input(
    "type in a meaningful word with uppercase and lowercase letters.\nEg:ChOClAtE"
)
password_ptwo = input("type in 4 numbers.\nEg:5481")
password_pthree = input("type in a special character.\nEg:@")
password_pfour = input("type in a word with uppercase and lowercase letters.\nEg:LiFT")
u = password_pone + password_ptwo + password_pthree + password_pfour
print(f"YAY!Your password is ready! It is {u}")
