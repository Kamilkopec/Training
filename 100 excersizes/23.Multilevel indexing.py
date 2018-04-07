# access the third value of key b from the dictionary,
from pprint import pprint

d = dict(a=list(range(1, 11)), b=list(range(11, 22)), c=list(range(21, 31)))

print(list(d.get('b')))
print(d['b'][2])
