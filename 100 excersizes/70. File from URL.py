# print out the text of this file
# http://www.pythonhow.com/data/universe.txt.
# please dont manually download the file. let python do all the work

import requests

reponse = requests.get('http://www.pythonhow.com/data/universe.txt')
text = reponse.text
print(text)

