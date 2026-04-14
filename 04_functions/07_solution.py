# Problem: Write a function that takes variable number of arguments and returns their sum.

def addition(*args) :
    total = 0
    for x in args:
        total += x
    print(total)

addition(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
addition(10, 20, 30, 40)
addition(99, 999, 46)