# Sort without sort()

li_items = [12,45,85,1,465,56,896,598,458]

for x in range(len(li_items)):
    for y in range(len(li_items) -1 ):
        if li_items[y] > li_items[y + 1]:
            li_items[y], li_items[y + 1] = li_items[y + 1], li_items[y]

print(li_items)   
    