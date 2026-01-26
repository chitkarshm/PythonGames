# Adventure begins!🖥️🖥️🖥️
print(
    "...Welcome to Darsh's Choose Your Own Adventure Game! "
    "As you follow the story, you will choose your "
    "fortune or your fate.Good luck!\n\n"
)

print(
    "You find yourself in a dark room.There are two doors:"
    " a leafy door and a stone door.Which door do you choose?"
)

door_choice = input("leafy=leafy door or stone=stone door")

# leafy starts🍃
if door_choice == "leafy":
    print(
        "🍃🍃🍃...\nAwesome! You are now in a forest! There are three "
        "paths: "
        "Right path, Left path, and Forward path. You will need good luck for this one"
    )
    choice = input("Right path=right Left path= left and Forward" " path=forward")
    if choice == "right":
        print(
            "➡️➡️➡️...\n\n__________SUCCESS!!__________\nYay!You go right and "
            "find two portals."
            " They both combine and you go home!😀😀😀"
        )
    else:
        print(
            "⬅️⬅️⬅️/⬆️⬆️⬆️...\n\n__________GAME_OVER__________\nWhoops! You went the wrong"
            " way and got stuck!😭😭😭"
        )
# stone starts🪨
else:
    print(
        "🪨🪨🪨...\nNice! You went in the stone door and you went in a cave!You can either"
        " get out of the cave or go deeper.Which one?"
    )
    option = input("get out= out or Go deeper= deeper")

    if option == "out":
        print(
            "⬅️⬅️⬅️...\n\n__________GAME_OVER!__________\nToo bad! The cave collapsed "
            "and you got stuck.😭😭😭"
        )
    else:
        print(
            "↘️↘️↘️...\n\n__________SUCCESS!!__________Congrats!You went deeper and found a crystal "
            "and a portal. You took the crystal and went home!😀😀😀"
        )
print("🖥️ 🖥️ 🖥️=======STORY ENDED=======🖥️ 🖥️ 🖥️")
# story over 🖥️🖥️🖥️
