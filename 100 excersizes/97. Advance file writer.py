# create a program that asks the user to submit text reapeatedy,
# the program save the changes when user submits SAVE, but doesnt close
# program save the save and closes when user submits CLOSE

data = []
while True:

    value = input('To Save or quite: SAVE or CLOSE \n''Enter a value:')

    if value != 'SAVE' and value != 'CLOSE':
        data.append(value)
    elif value == 'SAVE':
        with open('user_data.txt', 'a+') as file:
            for element in data:
                file.writelines(element + '\n')
            data.clear()
            print('Elements saved')
    else:
        with open('user_data.txt', 'a+') as file:
            for element in data:
                file.writelines(element)
        break

