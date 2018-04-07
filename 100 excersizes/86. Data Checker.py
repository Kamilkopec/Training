# one of the items is not a country.
# please use Python and the file containing the loist of countruies
# as data source to filter out the checklist of non-country items
# Once you have filtered out checklist then print it out
# use the list of countries in file countries2.txt

checklist = ['Portugal', 'Germany', 'Munster', 'Spain']
checklist2 = []
countries = []

with open('countries2.txt', 'r') as file:
    reader = file.readlines()
    for line in reader:
        line = line.strip('\n')
        countries.append(line)

for check in checklist:
    if check in countries:
        checklist2.append(check)
print(checklist2)
