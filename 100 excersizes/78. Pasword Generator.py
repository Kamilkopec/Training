# create a program that generates a password of 6 random alphanumeric character
# in the range

import string
import random
my_range = string.ascii_lowercase + string.ascii_uppercase + string.digits


x = random.choices(my_range, k=6)
print("".join(x))




