order_size = input("Please enter coffee size ? ")
extra_shot = input("Please enter extra shot ? ").strip().lower()

extraShotOutput = ""

if extra_shot == "true" :
    extraShotOutput = True
elif extra_shot == "false":
    extraShotOutput = False
else :
    print("Invalid")


if extraShotOutput : 
    print("Coffee with extra shot")
else :
    print("Coffee without extra Shot")