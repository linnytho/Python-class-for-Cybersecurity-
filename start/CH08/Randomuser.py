import http.client
import json

conn = http.client.HTTPSConnection("randomuser.me")

conn.request("GET", "/api/")

res = conn.getresponse()
data = res.read()

#print(data.decode("utf-8"))

Random_user = json.loads(data.decode("utf-8"))

user = Random_user["results"][0]
print("USER INFORMATION")

print("PERSONAL INFORMATION")
print("Gender:", user["gender"])
print("Name", user["name"]["title"],user["name"]["first"], user["name"]["last"])

print("LOCATION")
print("Street Number:", user["location"]["street"]["number"])
print("Street Name:", user["location"]["street"]["name"])
print("City:", user["location"]["city"])
print("State:", user["location"]["state"])
print("Country:", user["location"]["country"])
print("Postcode:", user["location"]["postcode"])

print("TIME ZONE")
print("Offset:", user["location"]["timezone"]["offset"])
print("Description:", user["location"]["timezone"]["description"])

print("ACCOUNT INFORMATION")
print("Email:", user["email"])
print("UUID:", user["login"]["uuid"])
print("Username:", user["login"]["username"])
print("Password:", user["login"]["password"])
print("Salt:", user["login"]["salt"])
print("MD5:", user["login"]["md5"])
print("SHA-1:", user["login"]["sha1"])
print("SHA-256:", user["login"]["sha256"])

print("REGISTRATION INFORMATION")
print("Date of Birth:", user["dob"]["date"])
print("Age:", user["dob"]["age"])
print("Registered Date:", user["registered"]["date"])
print("Registered Age:", user["registered"]["age"])
print("Phone:", user["phone"])
print("Cell:", user["cell"])
print("ID Name:", user["id"]["name"])
print("ID Value:", user["id"]["value"])