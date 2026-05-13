# Leap Year Checker


year = int(input("Please enter a year ? "))

def leap_year(y):
    if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
        return True
    else :
        return False
    
print(leap_year(year))