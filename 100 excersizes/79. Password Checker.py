# create a script that lets the user submit a password untill they have
# satisfied three conditions:
# 1. Pasword contains at least one numer
# 2. contains one uppercae letter
# 3. its is at least 5 chars long
# print out message 'password is not fine' if false

import string
import ascii

upper = string.ascii_uppercase
numbers = '0123456789'



while True:
    psw = list(input("Input your password"))

    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print('Pasword is fine')
        break
    else:
        print("Password is not fine")








