# import the dictionary in a json file

import json, pprint


with open('company1.json', 'r') as file:
    f = json.load(file)

pprint.pprint(f)
