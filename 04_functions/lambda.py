# Global variable
x = 10

def modify_var():
    
    global x # use global to make a varibale global
    x = 20

modify_var()
print(x)


# lambda arguments: expression


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.