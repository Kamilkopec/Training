# create a fuction that takes a text file as input and returns the number of words
# contained in the text file. some words can be seperated by a comma with no space.


def count_words(filename):
    with open(filename, 'r') as file:
        reader = file.read()
        new = reader.replace(',', " ")
        new_split = new.split(" ")
        return len(new_split)

print(count_words('words2.txt'))

# alternative is to use the re modue


import re


def count_words2(filename1):
    with open(filename1, 'r') as file:
        reader = file.read()
        new = reader.replace(',', " ")
        new_split = re.split(",|", new)
        return len(new_split)


print(count_words('words2.txt'))
