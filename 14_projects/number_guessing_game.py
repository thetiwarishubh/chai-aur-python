import random

guess = random.randint(1, 10)
count = 0
while True :
    choice = int(input("Guess the number ? "))

    if choice > 10 :
        print("Invalid number! Please enter 1 to 10")
        break

    count += 1
    if choice > guess :
        print("Number is too high")
    elif choice < guess :
        print("Number is Too low")
    else :
        print("Equal Number")
        print(f"You got the number {guess}, and count is {count}")
        break