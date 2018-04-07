# create a script that lets the user submit a password until they have satisfied three conditions:
# Password contains at least on number
# Contains one uppercase letter
# it is at least 5 chars long
# give the exact reason  why the user has not created a correct password
# before asking for password, ask for username

users_list = []


def psw_check():

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


def file_open():
    global users_list
    with open('users.txt', 'r') as file:
        reader = file.readlines()
        for line in reader:
            line = line[:-1]
            users_list.append(line)
    return users_list


file_open()

while True:

    user = input('Enter User name: ')
    file_open()
    if user in users_list:
        print('User already exists')
    else:
        psw_check()







