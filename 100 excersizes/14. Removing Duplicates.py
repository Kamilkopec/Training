# remove items from the list a

a = ["1", 1, "1", 2]

# a1= map(int, a)
print(list(set(a)))

# sets are data types where duplicates are not allowed
# converiting list to a set removes the duplicates automaticaly.

# solution 2
# if you need to preserve the order of the list you can use the solution below:

from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)

# solution 3 for loop

a = ["1", 1, "1", 2]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)