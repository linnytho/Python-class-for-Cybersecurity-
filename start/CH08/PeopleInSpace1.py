import requests

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
#print(response.json())

astronauts = response.json()

print(astronauts)

# Print number of people
print("Number of people in space:", astronauts["number"] )

# Print first person
print(f"The first person is {astronauts['people'][0]['name']}")

# print all people in space
people = astronauts["people"]
for person in people:
    print(f"{person['name']} is on {person['craft']}")

