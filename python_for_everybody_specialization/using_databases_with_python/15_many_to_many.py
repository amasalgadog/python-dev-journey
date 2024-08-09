import sqlite3

conn = sqlite3.connect('many-2-many.sqlite')
cur = conn.cursor()

cur.close()

conn.close()