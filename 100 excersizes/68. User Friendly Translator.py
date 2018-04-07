#create an english to portuguese translation program.
# the program takes a word form the user as input and traslates it
# using the following dictionary as a vocabuylary source.
# in addition, return the message 'we coulnt find that word. when the user enters a words,
# that is not in the dictionary. also, make the program non case sensitive.
# meaning that for example, both earth and Earth should retunr the translation correcly



d = dict(weather="clima", earth = "terra", rain = "chuva")

def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return 'blebleble'


word = input('Enter a word: ')
print(vocabulary(word.lower()))
