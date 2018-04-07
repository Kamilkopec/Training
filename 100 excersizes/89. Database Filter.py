# please download the database file database.db.
# @ the file contains a table with 50 country names along
# with their are in square km and population.
# @ use Python to print out those countries that have an are of greater than
# 2,000,000

import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

condition = c.execute('SELECT country FROM countries WHERE area >= 2000000')
my_list = list(c.fetchall())

conn.close()

for i in my_list:
    print(i[0])
    print(type(i))