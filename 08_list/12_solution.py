# Remove duplicates

li_items = [45,78,45,78,"Shubham", "Shubh", "Shubh", True, True]

orginal_item = list(set(li_items))
print(orginal_item)

# 2nd Method

new_original_items = []
for x in range(len(li_items)):
    if li_items[x] not in new_original_items:
        new_original_items.append(li_items[x])

print(new_original_items)