questions = [
    "Who is the Lord of Winterfell at the start of the series? ",
    "What is the motto of House Stark? ",
    "What are the names of Daenerys three dragons? ",
    "Who kills Joffrey Baratheon? ",
    "What is the name of Aryas sword? ",
    "Which house does Tyrion Lannister belong to? ",
    "What is beyond the Wall? ",
    "Who sits on the Iron Throne at the very end? "
]

answers = [
    "eddard stark",
    "winter is coming",
    "drogon rhaegal viserion",
    "olenna tyrell",
    "needle",
    "lannister",
    "the white walkers",
    "bran stark"
]

score = 0

for i in range(len(questions)):
    reply = input(questions[i]).lower()
    if reply == answers[i]:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The answer was " + answers[i])

print("You scored " + str(score) + " out of " + str(len(questions)))
