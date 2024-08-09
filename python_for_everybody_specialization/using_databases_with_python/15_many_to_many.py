import sqlite3

conn = sqlite3.connect('many-2-many.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Person')
cur.execute('''
            CREATE TABLE Person (
            id INTEGER NOT NULL UNIQUE,
            name TEXT, email TEXT,
            PRIMARY KEY (id AUTOINCREMENT)
            )''')

cur.execute('DROP TABLE IF EXISTS Book')
cur.execute('''
            CREATE TABLE Book (
            id INTEGER NOT NULL UNIQUE,
            title TEXT,
            PRIMARY KEY (id AUTOINCREMENT)
            )''')

cur.close()
conn.close()