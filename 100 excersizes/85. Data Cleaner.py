# clean the list with python by generating a new text file.
# file should contain list of country names without any other text
# or break lines in it.


import string
ble = []
upper = list(string.ascii_uppercase)

with open('countries-raw.txt', 'r') as file:
    reader = file.readlines()
    for line in reader:
        line = line.strip('\n')
        if not line == "" and line not in upper and not line == 'Top of Page':
            ble.append(line)
with open('countries2.txt', 'w') as new_file:
    for i in ble:
        new_file.writelines(i + '\n')





