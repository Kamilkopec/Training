# create an English to Portuguese translation program.
# the program takes a word from the user as input and translates it using the following
# dictionary as a vocabulary source

d = dict(weather='clima', earth='terra', rain='chuva')

word = input('Enter a word: ')

if word in d.keys():
    print(d.get(word))
else:
    print('no such word in the dictionary')


# solution from Udemy

d = dict(weather='clima', earth='terra', rain='chuva')


def vocabulary(word):
    return d[word]


word = input('Enter word: ')
print(vocabulary(word))
