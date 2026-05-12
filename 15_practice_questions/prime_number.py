num = int(input("Enter a number ? "))

def prime_number(num):
    if num <= 1:
        return "Not prime"
    
    for x in range(2, num):
        if num % x == 0 :
            return "Not Prime"
    
    return "Prime"

print(prime_number(num))