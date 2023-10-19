import json
from OOP.assets.helper import FreeSpace

# Convert JSON to Python
identity = '{ "name" : "Daniel", "age" : 20, "hobby" : "Playing Game"}'

identityPython = json.loads(identity)

print(identityPython["name"])
print(identityPython["age"])
print(identityPython["hobby"])

FreeSpace()

# Convert Python to JSON
order = {
    "food" : "burger",
    "drink" : "soda"
}

orderJson = json.dumps(order)
print(orderJson)

FreeSpace()

# Convert Python objects into JSON strings
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

FreeSpace()

# Format and Order the result
x = {
  "name" : "John",
  "age" : 30,
  "pets" : "Cat",
  "cars" : [
    {"model" : "BMW 230", "mpg": 27.5},
    {"model" : "Ford Edge", "mpg": 24.1}
  ],
  "Bike" : [
      {"model" : "Honda Vario 150", "year" : "2019"},
      {"model" : "Honda Supra", "year" : "2005"}
  ] 
}
# separators(end, sep), sort_keys = mengurutkan
print(json.dumps(x, indent=3, separators=(".", " = "), sort_keys=False)) 

FreeSpace()