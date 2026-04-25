import random

dice_count = 0
while True : 
    choice = input("Do you want to play (Y/N) ?").lower()

    if choice == "y" :
        print(f"({random.randint(1, 6)}, {random.randint(1, 6)})")
        dice_count += 1
    elif choice == "n" :
        print("Thank You for Playing!")
        print(dice_count)
        break
    else :
        print("Invalid Syntax!")



    




