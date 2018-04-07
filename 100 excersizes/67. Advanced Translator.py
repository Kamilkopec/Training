# create an english to port translation program.
# the program takes a word from the user as input and translates it usign
# the following dictionary as a vocabulary source.
# in addition, try to return the message 'we couldnt find that word,
# whn user enters a word that is not in the dictionary.

d = dict(weather='clima', earth='terra', rain='chuva')


def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return 'Ble ble ble'


word = input('Enter word: ')
print(vocabulary(word))


