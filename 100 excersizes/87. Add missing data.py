# add missing data to the file

checklist = ['Portugal', 'Germany', 'Spain']
country_list = []

with open('countries-missing.txt', 'r+') as file:
    reader = file.readlines()
    for line in reader:
        line = line.strip('\n')
        country_list.append(line)
    for i in checklist:
        if i not in country_list:
            file.writelines('\n' + i)

