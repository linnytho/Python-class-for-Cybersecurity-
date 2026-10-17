#!/usr/bin/env python3
# Sample script that writes to a file
# By 

# import 
import os 

# get current dirrectory 
script_path = os.path.abspath(__file__)
script_dir = os.path .dirname(script_path)

# Build file path 
file_path = os.path.join(script_dir, "testfile.txt")

# Open file for waiting 
f = open(file_path, "w")

# Write to the file 
f.write("Hello World\n")
f.write("My name is Linny\n")
f.write("I like rubber ducks\n")

#Close file 
f.close()