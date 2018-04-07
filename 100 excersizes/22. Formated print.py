# create a dictionary of keys a, b, c where each key has a value a list from 1 to 10,
# 11 to 20, and 21 to 30 respectively and print out
import pprint as niceprint
keys = ['a', 'b', 'c']
my_dict = {}

a = 0
b = 11

for key in keys:
    my_dict[key] = list(range(a, b))
    a = int(list(range(a, b))[-1]) + 1
    b = a + 10

niceprint.pprint(my_dict, indent=1)

