import json

d = {
    'foo': 'bar',
    'alice': 1,
    'wonderland': [1, 2, 3]
}

with open("ss", 'r') as f:
    j = json.load(f)
    print(type(j))
    print(j)