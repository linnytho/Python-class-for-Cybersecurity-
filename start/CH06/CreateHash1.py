#!/usr/bin/env python3
# Script that hashes a password
# By 

from passlib.hash import sha512_crypt

salt = input("Salt (KCZ30T.pBobQcvvd):") or "KCZ30T.pBobQcvvd"
password = input("Password (Password01):") or "Password01"

hashed_pass = sha512_crypt.using(rounds=5000).hash(password, salt=salt)

print(hashed_pass)