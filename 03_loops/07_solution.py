while True:
    try:
        user_input = int(input("Please enter a number between 1 and 10"))

        if 1 <= user_input <= 10 :
            print(f"Thank you! You entered {user_input}.")
            break
        else :
            print(f"That number is not between a and 10. Try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric integer.")