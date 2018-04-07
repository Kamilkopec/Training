# create a script that generates a file where all letters of alphabet are
# listed three in each line.


import string

letters = string.ascii_lowercase + " "

ble1 = letters[0::3]
ble2 = letters[1::3]
ble3 = letters[2::3]


with open('letters.txt', 'w') as file:
    for letter1, letter2, letter3 in zip(ble1, ble2, ble3):
        file.write(letter1 + letter2 + letter3 + '\n')


