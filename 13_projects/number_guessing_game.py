import random

guess = random.randint(1, 10)
count = 0
while True :
    choice = int(input("Guess the number ? "))
    count += 1
    if choice > guess :
        print("Number is too high")
    elif choice < guess :
        print("Number is Too low")
    else :
        print("Equal Number")
        print("The Count is ", count)
        break