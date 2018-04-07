# create a program that asks the user to submit text repeatedly
# the program closes when the user submits CLOSE
# then the file is beeing written

with open('user_data.txt', 'a+') as file:
    data = []
    value = ''
    while value != 'CLOSE':
        value = input('Enter a value, to exit enter CLOSE: ')
        data.append(value)
    for element in data:
        file.writelines(element + '\n')