# Sum of digits

num = int(input("Enter number ? "))

def sum_of_digits(x):
    total = 0
    while x > 0:
        total += x % 10
        x //= 10
    return total

print(sum_of_digits(num))

