# Second largest number
import random

numbers = [random.randint(1, 1000) for _ in range(1000)]

# print(numbers)



largest_number = numbers[0]
second_largest_number = numbers[0]

for x in range(len(numbers)):
    if largest_number < numbers[x] :
        second_largest_number = largest_number 
        largest_number = numbers[x]
    elif second_largest_number < numbers[x] and numbers[x] != largest_number:
        second_largest_number = numbers[x]


print(largest_number)
print(second_largest_number)