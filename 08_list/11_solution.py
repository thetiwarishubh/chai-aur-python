# Find max/min


# First Method

def max_min(x):
    max_num = max(x)
    min_num = min(x)
    return max_num, min_num

# print(max_min([12, 45,87, 658, 834, 36]))

# Second Method

def find_max_min(x):
    max_num = x[0]
    min_num = x[0]

    for i in range(len(x)):
        if max_num < x[i]:
            max_num = x[i]

    if min_num > x[i]:
        min_num = x[i]


    return max_num, min_num


print(find_max_min([12, 45,87, 658, 834, 36, 6, 3]))