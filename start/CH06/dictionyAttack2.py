import os
from passlib.hash import sha512_crypt

def load_dictionary(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.readlines()

def create_hash(password, salt):
    script_dir = os.path.dirname(os.path.adspath(__file__))
    shadow_path = os.path.join(script_dir, "shadow")

    if not os.path.exists(shadow_path):
        print("shadow file not found!")
        return
    
password_guesses = load_dictionary("top1000.txt")

with open(shadow_path, 'r', encodings = "utf-8", errors='ignore') as f:
    for sline in f:
        shadow_line = line.strip()
        if not shadow_line or ":" not in shadow_line:
            continue
            
        shadow_parts = shadow_line.split(":")
        user_name = shadow_parts[0]
        user_hash = shadow_parts[1]
        
        if "$" not in user_hash:
            continue
            
        user_salt = user_hash.split("$")[2]
        
        found_match = False
        for password_guess in password_guesses:
            hashed_guess = create_hash(password_guess.strip(), user_salt)
            if user_hash == hashed_guess:
                print(user_name, password_guess.strip())
                found_match = True
                break
                
        if not found_match:
            print(f"{user_name}: Not found")
