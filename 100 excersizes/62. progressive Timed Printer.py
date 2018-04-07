# create a program that once executed prints Hello instanlty first, then
# it prints it after 1 second, then after 2, 3, 4, and so on

import time

counter = 0
while True:
    time.sleep(counter)
    print('hello')
    counter += 1

