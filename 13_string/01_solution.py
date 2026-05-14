# Count vowels

str_input = input("Please Enter a string ? ")

def count_str(x):
    count = 0
    new_str = list(x)
    for i in range(len(new_str)):
        if new_str[i] == 'a' or new_str[i] == 'e' or new_str[i] == 'i' or new_str[i] == 'o' or new_str[i] == 'u' :
            count += 1
    return count
print(count_str(str_input))