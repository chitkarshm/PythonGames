def print_horizontal_line():
    print("---" * boardsize)


def print_vertical_line():
    print("|  _" * (boardsize + 1))


boardsize = int(input("What should your game board size be?"))
for index in range(boardsize):
    print_horizontal_line()
    print_vertical_line()
print("---" * boardsize)
