import hashlib
import requests
import secrets
import string


def generate_password():
    length = int(input("Enter password Length: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += secrets.choice(characters)
    print("Your random password is:", password)
    return password  # Returns the password so check_password can use it


def check_password(password):
    sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching API: {response.status_code}")
    if suffix in response.text:
        print("This password has been pwned!")
    else:
        print("This password seems safe.")

if __name__ == "__main__":
    my_password = generate_password()
    check_password(my_password)
