# the following code prints hello, checks if 2 is greated than 1 and then break the loop
# because 2 is actually greater than 1. therefore hi is not printed out.
# please replace break with somethinmg else so that hello is printed out repeatedly and hi
# is never printed

while True:
    print('hello')
    if 2 > 1:
        continue
    print('hi')