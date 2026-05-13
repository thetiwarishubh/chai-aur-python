# Largest of 3 numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))


def largest_number(x, y, z):
    if (x > y) and (x > z):
        largest = x
    elif (y > x) and (y > z):
        largest = y
    else :
        largest = z

    return f"The largest number is {largest}"

print(largest_number(num1, num2, num3))