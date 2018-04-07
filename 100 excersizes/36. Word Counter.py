# create a function that takes a text file as input and retunr number of words in that file


def count_word(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)


print(count_word('words1.txt'))
