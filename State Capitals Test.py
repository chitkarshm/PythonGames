import time
import random

_TIMEOUT_SECS=15

name = input("What is your name?")
print(f"Hi {name}! Welcome to the State Capitals Test!\nYou have to guess the capital of the state!!\nYou only have {_TIMEOUT_SECS} seconds to solve each problem\nIf you need help just say 'idk'")
time.sleep(4)
print("3,")
time.sleep(1)
print("2,")
time.sleep(1)
print("1,")
time.sleep(1)
print("START COOKING!!!")

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
    ("Idaho ", "Boise"),
    ("Illinois ", "Springfield"),
    ("Indiana ", "Indianapolis"),
    ("Iowa ", "Des Moines"),
    ("Kansas ", "Topeka"),
    ("Kentucky ", "Frankfort"),
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
    ("North Dakota ", "Bismarck"),
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
    ("Vermont ", "Montpelier"),
    ("Virginia ", "Richmond"),
    ("Washington ", "Olympia"),
    ("West Virginia ", "Charleston"),
    ("Wisconsin ", "Madison"),
    ("Wyoming ", "Cheyenne"),]

random.shuffle(question_answers)

def question_with_answer() -> tuple[str, str]:
    return (question_answers)[0]


turns = len(question_answers)
correct_count=0
index = 0
points = 0
while index < turns:
    ques,ans = question_answers[index]
    t_start = time.time()
    user_ans = input(ques)
    t_end = time.time()
    t_taken = t_end - t_start
    if user_ans == "I give up":
        print(f"Okay! Come again later! Your final score was {points}")
        break
    elif user_ans == "idk":
        print(f"The capital of {ques} is {ans}.")
        index += 1
        continue
    if ans == user_ans:
        if t_taken > _TIMEOUT_SECS:
            print(f"You got the answer right, but it was too late. You lost one point because you took {round(t_taken)} seconds. You have {points} points now.")
            points-=1
        else:
            points += 1
            correct_count += 1
            print(f"YAY! You have {points} points!")
    else:
        points = points - 1
        print(f"WRONG ANSWER!The correct answer was {ans}. You now have {points} points")
    index += 1
if index == turns:
    percentage= (correct_count/turns)*100
    if percentage >= 90:
        grade= "A!! You're a genius!!"
    elif percentage >= 80:
        grade= "B! Great job!"
    elif percentage >= 70:
        grade= "C! Not bad!"
    elif percentage >= 60:
        grade= "D. Keep practicing!"
    else:
        grade= "F. You should study more."
    print(f"Congrats {name}! You finished the entire list!!")
    print(f"Final Score: {points} points")
    print(f"{correct_count}/{turns} correct")
    print(f"Accuracy: {round(percentage)} %")
    print(f"Grade: {grade}")
    print(f"Goodbye {name}!")