import random

condition = True
while condition : 
    choice = input("Do you want to play (Y/N) ?").lower()

    if choice == "y" :
        print(f"({random.randint(1, 6)}, {random.randint(1, 6)})")
    elif choice == "n" :
        print("Thank You for Playing!")
        break
    else :
        print("Invalid Syntax!")



    




