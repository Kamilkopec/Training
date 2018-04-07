# download the urls.txt file.
# @ the file contains some broken URLs.
# remove s from https and add another forward slash next to the existing slash.
# so the content looks good.

with open('urls.txt', 'r') as file:
    reader = file.readlines()
    for row in reader:
        row = row.replace('\n', '')
        row = row.replace('https:/', 'http://')

        print(row)