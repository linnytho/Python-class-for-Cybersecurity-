#!/usr/bin/env python3
# Script that encrypts/decrypts text using cryptography module
# By Linny 10/21

# key 

from cryptography.fernet import Fernet

def create_key():
    key = Fernet.generate_key()
    key = key.decode()
    return key
def encrypt(key, plain_text):
    key = key.encode()
    plain_text = plain_text.encode()

    # Creat fernet object and encrypt
    f = Fernet(key)
    cipher_text = f.encrypt(plain_text)
    cipher_text = cipher_text.decode()
    return cipher_text
def decrypt(key, cipher_text):
    key = key.encode()
    plain_text = plain_text.encode()

    # Creat fernet object and encrypt
    f = Fernet(key)
    plain_text = f.decrypt(plain_text)
    plain_text = plain_text.decode()
    return plain_text

# Ask user what to do
print("""
      Welcome to the encrption tool
      This tool encrypts and decrypts data 
      This uses Frenet Encryption.""")
print("="*80)
action =  input("Encrypt, Decrypt, or Create key (e/d/c)")
action = action.lower()
action = action[0]

# if create key 
if action =="c":
    key = create_key()
    print(key)
    
#else if encrypt
elif action == "e":
   # Get key
   key = input("key: ")
   # Get message  
   message = input("Message: ")
   cipher_text = encrypt(key, message)
   print(cipher_text)
#else if decrpt 
elif action =="d":
   
   # Get key
   key = input("key: ")
   # Get message 
   message = input("Message: ")
   plain_text = encrypt(key, message)
   print(plain_text)




#key = Fernet.generate_key()
#print(key)

#f = Fernet(key)
#plain_text = b"this is my secret"
#cipher_text = f.encrypt(plain_text)

#print(cipher_text)

#print(f.decrypt(cipher_text))