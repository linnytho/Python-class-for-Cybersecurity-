#!/usr/bin/env python3
# A simple "Hello World" script in python
# Created 9/28 by Ed

print("Hello World")


# Get user name- string concatenation
user_name = input("What is your name?")
# say hello to user
print("Hello" + user_name)

#Print out afffirmation "Today is going to be a great day"
print("Today is going to be a great day!")

# string formatting and f-string 
print ("Hello {0}".format(user_name))
print (f"Hello {user_name}")

# multiple print statements
print("Hello", user_name)
message = "Hello" + user_name
print(message)
# Removing newline
print ("Hello", end = "" )
print (user_name)

# old style
print ("Hello %s" % user_name)

# Joining text
print("".join(["Hello", user_name]))

 

