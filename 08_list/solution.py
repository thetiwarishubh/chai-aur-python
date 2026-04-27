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

# number = [100, 50, 400, 500]
# number[1] = 200
# print(number)
# number.append(600)
# print(number)

# number.insert(2, 300) 
# print(number)

# number.remove(600)
# print(number)

# del number[0]
# print(number)


"""
Exercise 3. Sum and Average of All Numbers in a List
Practice Problem: Calculate the total sum of all integers in a list and find the arithmetic mean (average).

Exercise Purpose: Aggregation is the heart of data science. This exercise teaches you how to reduce a collection of multiple data points into a single, meaningful summary statistic.
"""

arr = [10, 20, 30, 40, 50]

total = sum(arr)
average = total/len(arr)
print(total) #150
print(average) # 30.0



"""

Exercise 4. Find Maximum and Minimum from List
Practice Problem: Identify the largest and smallest numerical values within a provided list.

Exercise Purpose: Finding extremes is vital for tasks like identifying the “best” price, the “highest” score, or detecting “outlier” data points in a dataset.

Given Input: Data: [45, 12, 89, 2, 67]

"""

data = [45, 12, 89, 2, 67]

print(max(data))
print(min(data))




"""
Exercise 5. Calculate the Product of All Elements
Practice Problem: Multiply every number in a list together to find the total product.

Exercise Purpose: While sum is built-in, “product” often requires you to think about how to accumulate values. This exercise reinforces the concept of an “accumulator variable” in a loop.

Given Input: Factors: [2, 3, 5, 7]

"""

data5 = [2, 3, 5, 7]
total5 = 1
for x in data5 :
    total5 *= x

print(total5)



"""
Exercise 6. Count Even and Odd Numbers
Practice Problem: Given a list of integers, iterate through the items and count how many are even and how many are odd.

Exercise Purpose: This introduces Flow Control and the Modulo Operator. It is a classic “Filtering” pattern where you categorize data based on a mathematical property. In real-world apps, this is the foundation for things like alternating row colors in a table or batching jobs into two different queues.

Given Input: Numbers: [10, 21, 4, 45, 66, 93, 11]

"""

data6 = [10, 21, 4, 45, 66, 93, 11]
odd = 0
even = 0

for x in data6 :
    if x % 2 == 0 :
        even += 1
    else :
        odd += 1


print(f"Even Numbers {even}")
print(f"Odd Numbers {odd}")


"""
Exercise 7. Reverse a List
Practice Problem: Take a list and reverse the order of its elements.

Exercise Purpose: Reversal is a fundamental operation in data structures (like reversing a string or a linked list). Python provides multiple ways to do this, and understanding the difference between In-place Reversal (changing the original) and Slicing (creating a new one) is crucial for memory management.

Given Input: List: [100, 200, 300, 400, 500]

Expected Output: Reversed List: [500, 400, 300, 200, 100]

"""
data7 = [100, 200, 300, 400, 500]

data7.reverse()
# list(reversed(data7))
print(data7)
