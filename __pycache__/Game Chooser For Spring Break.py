import random

games = ["Sriracha", "Go Fish", "Caram", "Scrabble", "Mario Monopoly","Trouble"]
choices = list(games)

while True:
    random.shuffle(choices)
    current_game = random.choice(choices)
    print(f"\nYou will play... {current_game}!")
    
    vote = int(input("How many votes? "))

    if vote >= 2:
        print(f"\nWell, then you will play {current_game}!")
        break
    else:
        choices.remove(current_game)
        
        if not choices:
            print("\nYou rejected everything!")
            print("Restarting the list. Actually vote this time!")
            choices = list(games) 
