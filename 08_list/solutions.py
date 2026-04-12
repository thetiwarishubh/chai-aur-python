


l = [34, 58, -85, -32, 65, -75]

positive = []
negative = []

for i in l :
    if i < 0 :
        negative.append(i)
    else :
        positive.append(i)

print(positive)
print(negative)


# Average of lists
l = [546, 865, 967, 874, 74, 4, 65, 73, 874]
sum = 0

for x in l :
    sum += x

sum /= len(l)

print(round(sum,1))

# find the greatest element and print its index too.

l = [57, 689, 894, 96, 64, 875, 73, 7, 943]

great = l[0]
index = 0

for i in range(len(l)):
    if l[i] > great :
        great = l[i]
        index = i
        

print(great)
print(index)

# find the second greatest element and print its index too.

l = [57, 689, 894, 96, 64, 875, 73, 7, 943, 912]

largest = l[0]
sec_largest = l[0]

for i in l :
    if i > largest :
        sec_largest = largest
        largest = i
    elif i > sec_largest :
        sec_largest = i

print(f"The second largest number is {sec_largest} and largest number is {largest}")



# check if list is sorted or not.

l = [57, 689, 894, 96, 64, 875, 73, 7, 943, 912]

for i in range(len(l) -1 ):
    if l[i] < l[i + 1] :
        continue
    else :
        print("Your list is not sorted")
        break
else :
    print("Your list is sorted")