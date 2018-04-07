# download the datase file and the ten_more_countries.txt file.
# then, add the rows of the txt to db

import sqlite3
import pandas

df = pandas.read_csv('ten-more-countries.txt')

conn = sqlite3.connect('database.db')
cur = conn.cursor()

for id, row in df.iterrows():
    print(row['Country'], row["Area"])
    cur.execute('INSERT INTO countries VALUES(NULL,?,?,NULL)', (row['Country'], row['Area']))
conn.commit()
conn.close()