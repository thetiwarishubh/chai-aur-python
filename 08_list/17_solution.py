# Merge two lists

li_one = [12,45,85,1,465,56,896,598,458]
li_two = [102,415,825,31,65,66,876,588,498]

#1st method

combined = li_one + li_two
print(combined)


# 2nd Method
li_one.extend(li_two)
print(li_one)

# 3rd Method
unpack_combined = [*li_one, * li_two]
print(unpack_combined)

