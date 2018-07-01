import fido
from pprint import pprint

f = fido.Fetch()
f.get("https://httpbin.org/get")

print(f.status)
print(f.text)
pprint(f.json())

f.post("https://httpbin.org/post", body={"hello":"world"})

print(f.status)
print(f.text)
pprint(f.json())

f.post("https://httpbin.org/post", 
            form={"username":"jsmith", "password":"abc123"})

print(f.status)
print(f.text)
pprint(f.json())