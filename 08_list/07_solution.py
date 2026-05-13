# Factorial

num = int(input("Enter a number ? "))


def factorial(x):
    fact = 1
    for i in range(x, 0, -1):
        fact *= i
    
    return fact

print(factorial(num))