items = ["apple", "banana", "orange", "apple", "mango"]

seen = set()

for item in items:
    if item in seen :
        print("Duplicate found", item)
        break
    seen.add(item)