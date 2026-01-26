import time
import random

_TIMEOUT_SECS=15

name = input("What is your name?")
print(f"Hi {name}! Welcome to the State Capitals Test!\nYou have to guess the capital of the state!!\n3,")
time.sleep(1)
print("2,")
time.sleep(1)
print("1,")
time.sleep(1)
print("START GUESSING!!!")
print(f"Also you only have {_TIMEOUT_SECS} seconds to solve each problem\n")

question_answers = [
    ("Alabama ", "Montgomery"),
    ("Alaska ", "Juneau"),
    ("Arizona ", "Phoenix"),
    ("Arkansas ","Little Rock",),
    ("California ", "Sacramento"),
    ("Colorado ", "Denver"),
    ("Connecticut ", "Hartford"),
    ("Delaware ", "Dover"),
    ("Florida ", "Tallahassee"),
    ("Georgia ", "Atlanta"),
    ("Hawaii ", "Honolulu"),
    ("Illinois ", "Springfield"),
    ("Indiana ", "Indianapolis"),
    ("Idaho ", "Boise"),
    ("Louisiana ","Baton Rouge",),
    ("Maine ", "Augusta"),
    ("Maryland ", "Annapolis",),
    ("Massachusetts ","Boston",),
    ("Michigan ","Lansing",),
    ("Minnesota ", "St. Paul"),
    ("Mississippi ", "Jackson"),
    ("Missouri ", "Jefferson City"),
    ("Montana ", "Helena"),
    ("Nebraska ", "Lincoln"),
    ("Nevada ", "Carson City"),
    ("New Hampshire ", "Concord"),
    ("New Jersey ", "Trenton"),
    ("New Mexico ", "Santa Fe"),
    ("New York ", "Albany"),
    ("North Carolina ", "Raleigh"),
    ("North Dakota ", "Bismark"),
    ("Ohio ", "Columbus"),
    ("Oklahoma ", "Oklahoma City"),
    ("Oregon ", "Salem"),
    ("Pennsylvania ", "Harrisburg"),
    ("Rhode Island ", "Providence"),
    ("South Carolina ", "Columbia"),
    ("South Dakota ", "Pierre"),
    ("Tennessee ", "Nashville"),
    ("Texas ", "Austin"),
    ("Utah ", "Salt Lake City"),
    ("Vermont ", "Montpeiler"),
    ("Virginia ", "Richmond"),
    ("Washington ", "Olympia"),
    ("West Virginia ", "Charleston"),
    ("Wisconsin ", "Madison"),
    ("Wyoming ", "Cheyenne"),
]


def random_question_with_answer() -> tuple[str, str]:
    return random.choices(question_answers)[0]


turns = 100000000
index = 0
points = 0
while index < turns:
    index += 1
    ques, ans = random_question_with_answer()
    t_start = time.time()
    user_ans = input(ques)
    t_end = time.time()
    t_taken = t_end - t_start
    if user_ans == "I give up":
        print(f"Okay! Come again later! Your final score was {points}")
        break
    if ans == user_ans:
        if t_taken > _TIMEOUT_SECS:
            print(f"You got the answer right, but it was too late. You lost all your points because you took {round(t_taken)} seconds.")
            points=0
        else:
            points += 1
            print(f"YAY! You have {points} points!")
    else:
        print(f"WRONG ANSWER!The correct answer was {ans}")
        points=0
