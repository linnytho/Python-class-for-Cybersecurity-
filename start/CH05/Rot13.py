#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By linny 10/19

# Ask for message 
source_message = input("What is the message or encryt/decrypt?")
source_message = source_message.lower()
final_message = ""
# For each letter
for letter in source_message:
    # convert letter to number
    ascii_num = ord(letter)

    # If its a letter, add13
    if ascii_num > 97:
        ascii_num = ascii_num + 13
 
    # if past z, wrap around
    if ascii_num > 122:
        ascii_num = ascii_num - 26

    # Convert number to letter 
    new_letter = chr(ascii_num)

    # Append letter to newmsg
    final_message = final_message + new_letter

# print  newsmg
print(final_message)