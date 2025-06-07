import random


def randstr():
    return random.choices(
        [
            "It is certain.",
            "It is decidedly so.",
            "As I see it, yes.",
            "Yes, definitely.",
            "You may rely on it.",
            "Most likely.",
            "Outlook good.",
            "Yes!",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don’t count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",
            "No.",
            "Maybe.",
            "Yeahh,no.",
        ]
    )[0]


input("Welcome to the Magic 8 Ball™️!\nGo ahead and ask your question!\n")
print("🎱🎱🎱...")
print(randstr())