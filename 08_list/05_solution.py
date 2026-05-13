# Reverse String

choice = input("Enter a string ? ")

def check_reversed_string(x):
    reversed_str = x[::-1]
    if reversed_str == x:
        return "True"
    else :
        return "False"

print(check_reversed_string(choice))