# print 1 - 100

for x in range(1, 101) :
    # print(x)
    pass


# sum of 1 to N

sum = 0
for x in range(1, 101):
    sum += x

# print(sum)

# Print Multiplication table (user input)

num = int(input("Please enter number ? "))

for x in range(1, 11) :
    print(f"{num} * {x} = {num * x}")



# Factorial of a number

fact = int(input("Please enter a num ? "))
fact_num = 1
for x in range(fact , 0, -1) :
    fact_num *=  x

print(fact_num)