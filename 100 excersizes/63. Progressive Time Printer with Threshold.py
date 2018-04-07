# create a progream that once executed the programs prints hello instantly first,
# then it prints it after 1 second, thenm after 2,3 and then the program prints out the messagr end of the loop
# and stops

import time

counter = 0
while counter <= 3:
    time.sleep(counter)
    print('hello')
    counter += 1
print('End of the loop')

