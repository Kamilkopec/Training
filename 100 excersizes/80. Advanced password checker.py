# create a script that lets the user submit a password
# until they have satisfiedthree conditions:
# 1. password contains at least one number
# 2. Contains one uppercase letter
# 3. it is at least 5 chars long
# give the exact reason why the user has not created a correct password


while True:
    notes = []
    psw = input('Enter Password: ')

    if not any(i.isdigit() for i in psw):
        notes.append('You need at least one number')
    if not any(i.isupper() for i in psw):
        notes.append('You need at least one upper letter')
    if len(psw) < 5:
        notes.append('You need at least 5 characters')
    if len(notes) == 0:
        print('Password is fine')
        break
    else:
        print('Please check the following: ')
        for note in notes:
            print(note)
