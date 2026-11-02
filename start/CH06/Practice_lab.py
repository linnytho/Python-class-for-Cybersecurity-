

import os

def read_entire_dictionary(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    count = 0

    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            password = line.strip()

            if not password:
                continue

            count += 1

            if count % 100000 == 0:
                print(f"Read {count:,} passwords.")

    print(f"\nFinished reading {count:,} passwords.")


read_entire_dictionary("top10000000.txt")

