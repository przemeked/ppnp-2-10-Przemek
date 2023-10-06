# json - {"name":"Radek}
# obiket typu klucz warotsc

import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))

dict_json = json.dumps(person_dict)
print(dict_json)
print(type(dict_json))

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)

with open('nasze_dane.json', 'r') as f:
    data = json.load(f)

print(data)
print(type(data))

print(data.keys())
print(data.values())
print(data.items())

print(data['name'])
