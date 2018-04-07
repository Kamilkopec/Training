# create a script that asks the user to enter their age and script calclulates
# user year of birth and print out like a string.
# generate current year dynamically

import datetime

age = int(input('How old are you? :'))
current_year = int(datetime.datetime.now().year)
year_born = current_year - age

print('We think that your year of birth is {}'.format(year_born))

