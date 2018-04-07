# Create a program that asks the user to input values sperated by commas and
# store those values in a seperate line in a text file.

value = str(input('Enter values separated by , : '))
my_list = value.split(',')

print(my_list)


with open('misiak.txt', 'a+') as file:
    for elm in my_list:
        file.writelines(elm + '\n')
