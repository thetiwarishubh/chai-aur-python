animal = "cat"
year = 2

if animal == "dog":
    if year < 2:
        print("Puppy Food")
    else:
        print("Adult Dog Food")

elif animal == "cat":
    if year < 2:
        print("Kitten Food")
    elif year > 5:
        print("Senior Cat Food")
    else:
        print("Adult Cat Food")
