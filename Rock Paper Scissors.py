print(
    "WELCOME TO THE ROCK PAPER SCISSORS GAME!!YOU CAN CHOOSE FROM ROCK, PAPER, OR SCISSORS!!lET THE GAME BEGIN!!"
)
player1 = ""
player2 = ""


def compare(item_one, item_two):
    if item_one == item_two:
        print("IT'S A TIE!!")

    elif item_one == "rock":
        if item_two == "scissors":
            return "ROCK WINS!!"
        else:
            return "PAPER WINS!!"

    elif item_one == "scissors":
        if item_two == "paper":
            return "SCISSORS WIN!!"
        else:
            return "ROCK WINS!!"

    elif item_one == "paper":
        if item_two == "rock":
            return "PAPER WINS!!"
        else:
            return "SCISSORS WIN!!"
    else:
        return "SORRY, THAT IS NOT VALID.YOU HAVE NOT ENTERED ROCK, PAPER, OR SCISSORS."


player1choice = input("%s ROCK, PAPER, OR SCISSORS?" % player1)

player2choice = input("%s ROCK, PAPER, OR SCISSORS?" % player2)

print(compare(player1choice, player2choice))
