# Reverse list

numbers = [ 12, 45, 78, 23, 56, 89, 34, 67, 90, 11, 54, 32, 76, 98, 21, 43, 65, 87, 10, 29, 51, 73, 95, 14, 36, 58, 80, 27, 49, 71, 93, 16, 38, 60, 82, 19, 41, 63, 85, 24, 46, 68, 91, 13, 35, 57, 79, 22, 99, 24]


# 1st method
numbers.reverse()
print(numbers)

# 2nd Method
reversed_list = list(reversed(numbers))
print(reversed_list)


# 3rd method
print(numbers[::-1])



# 4th Method
new_reversed_list = []

for x in range(len(numbers)-1, -1, -1):
    new_reversed_list.append(numbers[x])

print(new_reversed_list)