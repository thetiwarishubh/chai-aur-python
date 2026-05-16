# In Python, a string is an immutable sequence of Unicode characters used to store and manipulate text.  The formal type name is str, and strings are created by enclosing characters in single quotes ('), double quotes ("), or triple quotes (''' or """ for multi-line text)


user = " Shubham tiwari"


# string slicing

# start from 0 index to 3(not include)
print(user[:3])

# start from 3 index to last index
print(user[3:])



# Modify string

# convert upper case 
print(user.upper())

# convert lower case
print(user.lower())


# remove space

print(user.strip())

# replace string 

print(user.replace("t", "T"))


# convert string into list 
print(user.split())



# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)


# string all methods 

# The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
# Converts the first character to upper case

username = "Shubham Tiwari"
print(username.capitalize())


# casefold()
# Converts string into lower case
# The casefold() method returns a string where all the characters are lower case.

# This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.

print(username.casefold())




# The center() method will center align the string, using a specified character (space is default) as the fill character.

x = username.center(20)
print(x)



# The count() method returns the number of times a specified value appears in the string.

print(username.count("S"))

# .join()


testing = ["shubh", "tiwari"]

x = " ".join(testing)
print(x)


z = "shubham tiwari".title()
print(z)
