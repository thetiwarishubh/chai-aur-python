# Palindrome Checker


input_str = input("Enter a string ? ")

def palindrome_check(x):
    reversed_st = x[::-1]
    if x == reversed_st :
        return "True, This is a Palindrome, {x}"
    else :
        return f"False, This is not a Palindrome!, {x}"

print(palindrome_check(input_str))