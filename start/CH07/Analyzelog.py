import re
import os 
from collections import Counter

# Locate the access.log file
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
file_path = os.path.join(script_dir, "access.log" )

# Creat a counter for website resources
resource_count = Counter()

# Open and read the log file 
with open(file_path, "r", encoding="utf-8", errors="replace") as f:

    # Read the log file line by line
    for line in f:

        # Find the requested resource 
        match = re.search(r'"[A-Z]+\s+(\s+)\s+HTTP/[^"]+"', line)

        # Count each resource found 
        if match: 
            resource = match.group(1)
            resource_count[resource] += 1

# Generate the report
print("Most Popular website resources")

for resource, count in resource_count.most_common():
    print(f"{resource}: {count} visits")

print(f"Total unique resources: {len(resource_count)}")