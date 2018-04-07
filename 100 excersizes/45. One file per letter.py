# create a script that generataes 26 text file named a.txt, b.txt, an so on.
# each file should contain a letter reflecting its fine name.

import string, os

letters = list(string.ascii_lowercase)
print(letters)
print(len(letters))

i = 0
while i < len(letters):
    filename = letters[i] + '.txt'
    with open(filename, 'w+') as file:
        file.write(letters[i])
    i += 1

# from excersize

# if not os.path.exists('letters'):
#     os.makedirs('letters')
# for letter in string.ascii_lowercase:
#     with open('letters/' + letter + '.txt', 'w') as file:
#         file.write(letter + '\n')
