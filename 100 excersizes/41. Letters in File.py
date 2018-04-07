# create a script that generates a text file with all letters of an English alphabet
# inside it, one letter per line

import string

letters = list(string.ascii_lowercase)
print(letters)
print(len(letters))

with open('letters.txt', 'w') as file:
    for letter in letters:
        file.write(letter + '\n')




