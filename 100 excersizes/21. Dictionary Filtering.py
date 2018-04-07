# filter dictionary by removing all items with a value of grater than 1

d = {'a': 1,  'b': 2, 'c': 3}

# my_dict = {key:value for key, value in d.items() if value <= 1}
# print(my_dict)
my_dict = {}
for key, value in d.items():
    if value <= 1:
        my_dict.update({key: value})
    else:
        continue
print(my_dict)