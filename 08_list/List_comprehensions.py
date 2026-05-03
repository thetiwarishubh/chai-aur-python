# The basic syntax is [expression for item in iterable]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# Square 

square = [x**2 for x in range(10+1)]
print(square)