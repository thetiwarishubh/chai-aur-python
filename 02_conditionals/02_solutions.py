user_Age = int(input("Please enter user age ? "))
day = input("Please enter day ? ")
price = 12 if user_Age >= 18 else 8

if day == "wednesday" : 
    price -= 2
    print("Ticket price for you $", price)
else :
    print("Ticket price for you $", price)
