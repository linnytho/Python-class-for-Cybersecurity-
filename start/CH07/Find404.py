#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By linny, 11/2

# Open log file 
# import 
import os 

# get current dirrectory 
script_path = os.path.abspath(__file__)
script_dir = os.path .dirname(script_path)

# Build file path 
file_path = os.path.join(script_dir, "access.log")

# Open file for waiting 
f = open(file_path, "r")

# Read line by line
while True:
    line = f.readline()
    if not line:
        break 
    # Search for 404
    if "404" in line:
        # print
        print(line)

f.close 