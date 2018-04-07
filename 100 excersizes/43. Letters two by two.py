# create a script that generates a file where all letters of alphabet are
# listed two in each line.

import string

# letters = list(string.ascii_lowercase)
#
#
# with open('letters.txt', 'w') as file:
#     i = 0
#     j = 2
#     while j <= len(letters):
#         item = list(letters[i:j])
#         item = list(item)
#         for idx in item:
#             file.write(str(idx))
#         file.write('\n')
#         i += 2
#         j += 2
#

with open('letters.txt', 'w') as file:
    for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]):
        file.write(letter1 + letter2 + '\n')

# he first created a list of letters in step of 2
# then created a string in step of 2 starting from 1
# then he zipped added 1 +1 and aqdded n
# then writted to a file


