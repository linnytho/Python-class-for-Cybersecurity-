#!/usr/bin/env python3
# Sample script that reads from a file
# By 

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
f = open(file_path, "r")

# read content 
contents = f.read()
print(contents)

#close 
f.close()