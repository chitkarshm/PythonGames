import random


def darsh_movie_choice():
    return random.choices(
        [
            "kung fu panda episodes",
            "angry birds",
            "garfield movie",
            
        ]
    )[0]


def yashi_movie_choice():
    return random.choices(
        [
            "",
        ]
    )[0]


def ma_food_menu():
    return random.choices(
        [
            "",
        ]
    )[0]


def special_menu():
    return random.choices(
        [
            "keema pao",
            "dumplings w\ ramen",
            "ice cream",
            "pizza",
            "foccacia",
            "chocolate",
            "kebabs",
        ]
    )[0]


def other():
    return random.choices(
        [
            "",
        ]
    )[0]


list_choice = input(
    "Which thing do you want to choose: yashi, darsh, ma, special,or other?"
)
if list_choice == "yashi":
    print(yashi_movie_choice())


if list_choice == "darsh":
    print(darsh_movie_choice())


if list_choice == "ma":
    print(ma_food_menu())


if list_choice == "special":
    print(special_menu())


if list_choice == "other":
    print(other())
