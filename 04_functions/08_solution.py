# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


print_details(name = "Shubham", location = "Delhi")