# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math 

def calculate(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return f"Circle area is {round(area, 2)} and circumference is {round(circumference, 2)}"

print(calculate(12))

