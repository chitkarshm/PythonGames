import time
import random

name = input("What is your name?")
print(f"Hi {name}! Welcome to the Trivia Game™!\n3,")
time.sleep(1)
print("2,")
time.sleep(1)
print("1,")
time.sleep(1)
print("START GUESSING!!!")
print(
    "the answers are written in lowercase so if you type it with uppercase it will be wrong\nAlso you only have 30 seconds to solve each problem\n"
)

question_answers = [
    ("Who assassinated Abraham Lincoln?", "john wilkes booth"),
    ("What is the scientific name for the Northern Lights?", "aurora borealis"),
    ("What was the first Disney Princess movie?", "snow white"),
    (
        "Who invented the telephone?",
        "alexander graham bell",
    ),
    ("How many items are in a baker's dozen?", "thirteen"),
    ("What kind of dog is Scooby-Doo?", "great dane"),
    ("What is the fourth planet from the Sun?", "mars"),
    ("What is the longest river in the world?", "nile"),
    ("A bibliophile is someone who loves...", "books"),
    (" Who is the author behind the children's book Cat in the Hat?", "dr seuss"),
    ("What two primary colors can be mixed to make purple?", "red and blue"),
    ("How many legs do insects typically have?", "six"),
    (" Fill in the blank: Roses are red, violets are ____.", "blue"),
    ("What is the chemical symbol for oxygen?", "o"),
    (
        " What movie about a famous doll was the highest-grossing movie of 2023?",
        "barbie",
    ),
    ("What video game character has a brother named Luigi who wears green?", "mario"),
    ("Who is the Greek goddess of love?" "aphrodite",),
    (
        "Even though it has a bill, webbed feet, and lays eggs, what kind of animal is a platypus?",
        "mammal",
    ),
    (
        "What do the following have in common: Atlantic, Pacific, Indian, and Arctic?",
        "they all have water",
    ),
    ("What type of whale is actually a dolphin?", "orca"),
    ("What mathematical operation is represented by the symbol ÷?", "division"),
    ("Which planet is known as the Blue Planet?", "earth"),
    ("What are diamonds made of?", "carbon"),
    ("What is the capital of China?", "bejing"),
    ("What does a sommelier specialize in?", "wine"),
    ("How many lives are cats said to have?", "nine"),
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
    if t_taken > 30:
        print(
            f"Time's up! the correct answer is {ans}.You took {round(t_taken)} seconds."
        )
        break
    if ans == user_ans:
        points += 1
        print(f"YAY! You have {points} points!")
    else:
        print(f"WRONG ANSWER!The correct answer was {ans}")
        break
print("BYEE!")
