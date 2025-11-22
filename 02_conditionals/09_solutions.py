year = 2028

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("This is Leap year", year)
else : 
    print("This is not Leap Year", year)