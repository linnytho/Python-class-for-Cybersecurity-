#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By 

# import
from passlib.hash import sha512_crypt
import os 
import sys

# Load dictionary function 
def load_dictionary(file_name):
    

    # get current dirrectory 
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)

    # Build file path 
    file_path = os.path.join(script_dir, file_name)

    # Open file for waiting 
    f = open(file_path, "r")

    # read content 
    contents = f.readlines()
    return(contents)
# Create hash function
def create_hash(password, salt):
    hashed_pass = sha512_crypt.using(rounds=5000).hash(password, salt=salt)
    return hashed_pass

# Get input from user 


# Separate pieces
script_dir = os.path.dirname(__file__)
shadow_path = os.path.join(script_dir, "shadow")
with open(shadow_path, "r") as shadow_file:
    for shadow_line in shadow_file:
        shadow_line = shadow_line.strip()
        if not shadow_line or ":" not in shadow_line:
            continue
        shadow_parts = shadow_line.split(":")
        user_name = (shadow_parts[0])
        user_hash = (shadow_parts[1])
        if "$" not in user_hash:
            continue
        user_salt = user_hash.split("$")[2]

# Load dictionary 
password_guesses = load_dictionary("top10000000.txt")
# For each lines/guess
for password_guess in password_guesses:
    # Hash guess 

    hashed_guess = create_hash(password_guess.strip(), user_salt)
    # COmpare hash to guess
    if user_hash  == hashed_guess:
        # Print guess
        print(user_name, password_guess.strip())
        #quit 
        sys.exit()


# print not found 
print("Not found")