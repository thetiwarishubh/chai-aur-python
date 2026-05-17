# file handling

import os
# f = open("main.py")
# print(f.write("hi"))




with open("test1.txt", "w") as f:
    f.write("Hello this  is the test\n")


with open ("test1.txt") as f:
    print(f.read())



if os.path.exists("test2.txt"):
  os.remove("test2.txt")
else:
  print("The file does not exist")