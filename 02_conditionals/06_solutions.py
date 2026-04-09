distance = int(input("Please enter distance in km ? "))

if distance < 3 :
    print("Walk")
elif distance < 15 :
    print("Drive Bike")
else : 
    print("Drive Car")