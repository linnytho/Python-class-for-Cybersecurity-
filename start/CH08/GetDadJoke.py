import http.client
import json

conn = http.client.HTTPSConnection("icanhazdadjoke.com")

conn.request("GET", "/", headers={"Accept":"application/json"})

res = conn.getresponse()
data = res.read()

#print(data.decode("utf-8"))

Dad_Joke = json.loads(data.decode("utf-8"))

print ("Tell me a joke:", Dad_Joke["joke"])

