check = input("Enter a string ? ").lower()
def check_palindrome(x):
    reversed_str = x[::-1]
    return True if reversed_str == x else False

print(check_palindrome(check))


reversed_str = check[::-1]

if reversed_str == check:
    print("True")
else :
    print("False")



