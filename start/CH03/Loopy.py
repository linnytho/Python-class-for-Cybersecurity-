#!/usr/bin/env python3
# example workign with Loops
#By 

# simple loop
#for i in range (10):
#    print (i + 1)

# fruits = ["apple","banana","cherry"]
# for fruit in fruits:
#     print(fruit)
#     if fruit == "banana":
#         break
#     #comment
#     print("another")

fruits = ["apple","banana","cherry"]
adjectives = ["red","big","tasty"]
for fruit in fruits:
    for adj in adjectives:
        print(adj, fruit)
        
