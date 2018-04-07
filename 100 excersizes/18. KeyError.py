# why do we get a key error in the below script

d = {'Name': 'John', 'Surname': 'Smith'}

# print(d['Smith'])
# there is no key in dictionary d
# via [''] you access a key not a value
# if we would like to access Smith:
print(d['Surname'])