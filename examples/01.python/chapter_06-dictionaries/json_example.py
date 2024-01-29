import json

# some JSON:
jsonData =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
person = json.loads(jsonData)

# the result is a Python dictionary:
print(person["age"])


# a Python object (dict):
person = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
jsonData = json.dumps(person)

# the result is a JSON string:
print(jsonData)