# Even/Odd Checker

num = int(input("Please enter number ? "))

def even_odd_checker(x):
    if x % 2 == 0 :
        return f"Even {x}"
    else :
        return f"Odd {x}"
    
print(even_odd_checker(num))