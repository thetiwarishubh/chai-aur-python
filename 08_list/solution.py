""" 
Exercise 1. Perform Basic List Operations
Practice Problem: Write a script to perform the following three operations on given list

1. Access the third element of a list
2. List Length: Print the total number of items
3. Check if the list is empty 
"""

# numbers = [10, 20, 30, 40, 50]

# print(numbers[2])

# print(len(numbers))

# print(len(numbers) == 0)

"""
Exercise 2. Perform List Manipulation
Practice Problem: Take a given list and modify it through five specific actions:

1. Change Element: Change the second element of a list to 200 and print the updated list.
2. Append Element: Add 600 o the end of a list and print the new list.
3. Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
4. Remove Element (by value): Remove 600 from the list and print the list.
5. Remove Element (by index): Remove the element at index 0 from the list print the list.

"""

number = [100, 50, 400, 500]
number[1] = 200
print(number)
number.append(600)
print(number)

number.insert(2, 300) 
print(number)

number.remove(600)
print(number)

del number[0]
print(number)