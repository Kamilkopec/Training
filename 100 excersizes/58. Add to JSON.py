import json, pprint

f = {"employees": [{"firstName": "John", "lastName": "Doe"},
                   {"firstName": "Anna", "lastName": "Smith"},
                   {"firstName": "Peter", "lastName": "Jones"}],
     "owners": [{"firstName": "Jack", "lastName": "Petter"},
                {"firstName": "Jessy", "lastName": "Petter"}]}

with open('company1.json', 'w') as file:
    json.dump(f, file)


with open('company1.json', 'r') as file:
    f = json.load(file)

f['employees'].append({'firstName': 'Albert', 'lastName': 'Bert'})

with open('company1.json', 'w') as file:
    json.dump(f, file)

# from udemy

# file.seek(0)
# json.dump(f, file, indent=4, sort_keys=True)
# file.truncate() # delete everything under the cursor
