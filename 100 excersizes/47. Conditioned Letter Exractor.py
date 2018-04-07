# write a scrript that iterates through each of the 26 text files, checks if the letter instide
# the text file is in string 'python' and puts the letter ina a list if yes

import glob

letters = []
file_list = glob.glob('*.txt')

for filename in file_list:
    with open(filename, 'r') as file:
        reader = file.read()
        if reader in 'python':
            letters.append(reader.strip('\n'))
        else:
            continue
print(sorted(letters))
