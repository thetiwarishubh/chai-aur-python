# try :
#     num = int(input("Please enter number ? "))
#     result = 20/num
#     print(round(result, 1))  
# except ZeroDivisionError:
#     print("Error : Division by zero is not allowed")
# except ValueError:
#     print("Error : Please enter a valid integer")





age = int(input("Please enter your age ? "))

try :
    if age < 10 or age > 18 :
        raise ValueError("You're not eligible for the club")
    else :
        print("Welcome to the club")

except  Exception as Error:
    print(f"Got and -- {Error}")