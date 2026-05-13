# Prime Number Checker


num = int(input("Enter a number ? "))

def prime_number_checker(x):
    if x < 0 :
        return "Error"

    if x == 1 :
        return "False"
    elif x == 2 :
        return "True"
    elif x > 2 :
        for i in range(2, x):
            if x % i == 0:
                return "False"
        return "True"
            

print(prime_number_checker(num))