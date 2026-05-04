import random

options = ["r", "p", "s"]
names = {"r": "Rock", "p": "Paper", "s": "Scissors"}

user = input("Rock, Paper, Scissors? (r/p/s): ").lower()

if user not in options:
    print("Invalid input! Please choose r, p, or s.")
else:
    computer = random.choice(options)

    print(f"Computer chose : {names[computer]}")
    print(f"You chose : {names[user]}")

    if user == computer:
        print("It's a tie!")
    elif (user == "r" and computer == "s") or \
         (user == "s" and computer == "p") or \
         (user == "p" and computer == "r"):
        print("You win!")
    else:
        print("You lose!")