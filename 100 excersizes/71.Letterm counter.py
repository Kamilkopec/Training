# count the number of a characters in this text file

import requests

reponse = requests.get('http://www.pythonhow.com/data/universe.txt')
text = reponse.text
counter = text.count('a')
print(counter)
