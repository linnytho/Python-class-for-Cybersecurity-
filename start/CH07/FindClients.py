#!/usr/bin/env python3
# Script that scans web server logs for client addresses
# Use RegEx to find and report on most frequent users
# By 

# Import 
import os
import re 

# get current dirrectory 
script_path = os.path.abspath(__file__)
script_dir = os.path .dirname(script_path)

# Build file path 
file_path = os.path.join(script_dir, "access.log")

# Open file for waiting 
f = open(file_path, "r")

# open file for reading
log_lines = f.readlines()

# setup regex pattern \s\d\d\d\s
search_pattern = r"\.\./"
results_dict ={}

# loop through each line
for line in log_lines:
    # Search for pattern 
    m = re.search(search_pattern, line)
    if m:
        print(line)
        # put into ditionary 
        #result = m.group(1)
        #if result in results_dict.keys():
            #results_dict[result] += 1
        #else:
            #results_dict[result] = 1

# sort by frequency and print
#sorted_keys = sorted(results_dict, key=results_dict.get , reverse=False)
#for key in sorted_keys:
    #print(key, results_dict[key])
