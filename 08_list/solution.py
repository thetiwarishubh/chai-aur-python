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


"""
Exercise 8. Sort a List of Numbers
Practice Problem: Sort a list of numbers in ascending order (lowest to highest).

Exercise Purpose: Sorting is perhaps the most studied topic in Computer Science. It turns chaotic data into organized data, which is a prerequisite for high-speed search algorithms like Binary Search. Python uses Timsort, an efficient, hybrid sorting algorithm.

Given Input: Unsorted: [56, 12, 89, 3, 22]

Expected Output: Sorted List: [3, 12, 22, 56, 89] 

"""

numbers8 = [56, 12, 89, 3, 22]

numbers8.sort()
print(numbers8)



"""
Exercise 9. Create a Copy of a List
Practice Problem: Create a copy of an existing list so that modifying the copy does not change the original.

Exercise Purpose: This exercise addresses one of the most common “gotchas” for new Python programmers: Pass-by-Object-Reference. If you simply write list_b = list_a, both variables point to the same list in memory. Learning to “Clone” or “Copy” is vital for data integrity.

Given Input: Original: ["Apple", "Banana", "Cherry"]

"""

original_list = ["Apple", "Banana", "Cherry"]
copied_list = original_list.copy()
print(copied_list)
copied_list[0] = "Mango"
print(copied_list)
print(original_list)


"""
Exercise 10. Combine Two Lists
Practice Problem: Merge two separate lists into a single, unified list.

Exercise Purpose: Data often arrives in fragments from different sources (e.g., two different database queries). Combining or “Concatenating” them is the first step in data aggregation.

Given Input:

List A: ["Physics", "Chemistry"]
List B: ["Maths", "Biology"]
Expected Output: Combined List: ['Physics', 'Chemistry', 'Maths', 'Biology']

"""

list_a = ["Physics", "Chemistry"]
List_b = ["Maths", "Biology"]

joined_list = list_a + List_b
print(joined_list)


"""
Exercise 11. List Slicing: Extract Middle Elements
Practice Problem: Given a list, extract a “slice” containing the middle three elements.

Exercise Purpose: Slicing is one of Python’s most powerful features. Unlike many languages that require manual loops to copy array sub-sections, Python uses [start:stop] syntax. This forms the foundation for data windowing and pagination in web development.

Given Input: List: [10, 20, 30, 40, 50, 60, 70]

Expected Output: Middle Three: [30, 40, 50]

"""

list_elements = [10, 20, 30, 40, 50, 60, 70]

print(list_elements[2:5])
print(list_elements[::-1])

"""
Exercise 12. Swap Two Elements at Given Indices
Practice Problem: Write a script to swap the positions of two elements in a list based on their indices.

Exercise Purpose: Swapping is the heart of every sorting algorithm like Bubble Sort or Quick Sort. While other languages require a temporary variable to hold a value during the swap, Python offers an elegant, one-line tuple unpacking method that is faster to write and less error-prone.

Given Input:

List: [23, 65, 19, 90]
Indices to Swap: 0 and 2

"""

question12 = [23, 65, 19, 90]
question12[0], question12[2] = question12[2], question12[0]
print(question12)


"""
Exercise 13. Access Nested Lists (Simple Indexing)
Practice Problem: Given a “list of lists,” access a specific item hidden inside the inner list.

Exercise Purpose: This exercise teaches you to navigate Multi-dimensional Data. Think of nested lists like a spreadsheet (Rows and Columns) or a theater seating chart. To find a specific seat, you need the row and seat numbers.

Given Input:

Nested List: [[1, 2], [3, 4, 5], [6, 7]]
Goal: Access the number 5.
Expected Output: Accessed Value: 5

"""

question13 = [[1, 2], [3, 4, 5], [6, 7]]
print(question13[1][2])


"""
Exercise 14. Check if List Contains a Specific Item
Practice Problem: Write a check to see if a certain value exists within a list and print a message based on the result.

Exercise Purpose: This is a Membership Test. It’s the logic used for “Is this username taken?” or “Is this item in the shopping cart?” Python’s in operator makes this incredibly readable, almost like plain English.

Given Input:

Inventory: ["Laptop", "Mouse", "Monitor", "Keyboard"]
Target: "Tablet"
Expected Output: Is Tablet in inventory? False

"""

question14 = ["Laptop", "Mouse", "Monitor", "Keyboard"]

for x in question14 :
    if x == "Tablet" :
        print(True)
    else :
        print(False)

"""
Exercise 15. Find the Longest String in a List
Practice Problem: In a list of strings, identify which string has the most characters.

Exercise Purpose: This combines Iteration with Comparison. It teaches you how to evaluate an attribute of an object (its length) rather than just its raw value. This is used in text processing, UI layout, and data cleaning.

Given Input: Words: ["PHP", "Exercises", "Backend", "Python"]

Expected Output: Longest word: Exercises

"""

question15 = ["PHP", "Exercises", "Backend", "Python"]
longest_words = question15[0]

for x in question15 :
    if longest_words > x :
        longest_words = x

print(longest_words)