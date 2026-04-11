checkPrime = int(input("Please enter number ? "))

count = 0
for x in range(1, checkPrime + 1) :
    if checkPrime % x == 0 :
        count += 1

if count == 2 :
    print("Prime Number")
else :
    print("Not a Prime Number")