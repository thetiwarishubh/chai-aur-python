# Armstrong Number

num = int(input("Enter a number ? "))

def is_armstrong(x):
    digit = str(x)
    digits = len(digit)
    sum_of_powers = sum(int(digit) ** digits for digit in digit)
    return sum_of_powers == x


print(is_armstrong(num))