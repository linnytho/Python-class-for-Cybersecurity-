
import os
from passlib.hash import sha512_crypt

# Find the folder containing this Python script
script_dir = os.path.dirname(os.path.abspath(__file__))


def load_dictionary(filename):
    file_path = os.path.join(script_dir, filename)

    if not os.path.isfile(file_path):
        print(f"File not found: {filename}")
        return 0

    count = 0

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            if line.strip():
                count += 1

    return count


def load_shadow():
    file_path = os.path.join(script_dir, "shadow")
    accounts = []

    if not os.path.isfile(file_path):
        raise FileNotFoundError("shadow file not found.")

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            parts = line.strip().split(":")

            if len(parts) < 2:
                continue

            username = parts[0]
            password_hash = parts[1]

            if password_hash.startswith("$6$"):
                accounts.append({
                    "username": username,
                    "hash": password_hash
                })

    return accounts


def validate_hash(password_hash):
    try:
        sha512_crypt.from_string(password_hash)
        return True
    except (ValueError, TypeError):
        return False


def test_hash():
    print("\n========== SHA-512 TEST ==========")

    test_password = "example123"
    generated_hash = sha512_crypt.hash(test_password)

    if sha512_crypt.verify(test_password, generated_hash):
        print("PASS: Correct password verified.")
    else:
        print("FAIL: Correct password rejected.")

    if not sha512_crypt.verify("wrongpassword", generated_hash):
        print("PASS: Incorrect password rejected.")
    else:
        print("FAIL: Incorrect password accepted.")


def main():
    print("========== SHADOW FILE ==========")

    accounts = load_shadow()
    print(f"SHA-512 accounts found: {len(accounts)}")

    valid = 0
    invalid = 0

    for account in accounts:
        if validate_hash(account["hash"]):
            valid += 1
            status = "Valid"
        else:
            invalid += 1
            status = "Invalid"

        print(f"{account['username']}: {status}")

    print("\n========== HASH SUMMARY ==========")
    print(f"Valid hashes: {valid}")
    print(f"Invalid hashes: {invalid}")

    print("\n========== DICTIONARY FILES ==========")

    dictionary_files = [
        "top10.txt",
        "top100.txt",
        "top1000.txt",
        "top10000000.txt"
    ]

    for filename in dictionary_files:
        count = load_dictionary(filename)
        print(f"{filename}: {count:,} entries")

    test_hash()

    print("\n========== PROGRAM FINISHED ==========")


if __name__ == "__main__":
    main()



