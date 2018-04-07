# from the database.db and use Python to access the table rows that have an area of
# greater than 2 000 000. then export the rows to CSV
#
# import sqlite3
#
# conn = sqlite3.connect('database.db')
# c = conn.cursor()
#
# condition = c.execute('SELECT id, country, area, population FROM countries WHERE area >= 2000000')
# my_list = list(c.fetchall())
# my_csv = []
#
# with open('ble.csv', 'w')as file:
#     for row in my_list:
#         row = str(row)
#         row = row.replace("'", '')
#         row = row.replace(' ', '')
#         my_csv.append(row)
#     for element in my_csv:
#         file.write(element[1:-1] + '\n')

# solution from udemy

import sqlite3
import pandas

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute('SELECT * FROM countries WHERE area >= 2000000')
rows = cur.fetchall()
conn.close()

df = pandas.DataFrame.from_records(rows)
df.columns = ['Rank', 'Country', 'Area', 'Population']
df.to_csv('ble.csv', index=False)

