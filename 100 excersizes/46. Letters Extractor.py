# write a script that exracts letters from the 26 text files and put the letters ina list

# import string
#
# letters = list(string.ascii_lowercase)
# letter_list = []
# i = 0
# while i < len(letters):
#     filename = letters[i] + '.txt'
#     with open(filename, 'r') as file:
#         reader = file.read()
#         letter_list.append(reader)
#     i += 1
# print(letter_list)
#

# solution from udemy:

import glob

letters = []
file_list = glob.glob('*.txt')
print(file_list)

# for filename in file_list:
#     with open(filename, 'r') as file:
#         letters.append(file.read().strip('\n'))
#