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

# Author table is a junction table consisting in 2 foreign keys pointing to Book and Person
cur.execute('DROP TABLE IF EXISTS Author')
cur.execute('''
            CREATE TABLE Author (
            person_id INTEGER,
            book_id INTEGER,
            PRIMARY KEY (person_id, book_id)
            )''')
# this PRIMARY KEY operation with two fields (columns) is a combination that force it to be unique combination

cur.execute('''
            INSERT OR IGNORE INTO Person (name, email) VALUES ('J. R. R. Tolkien','jrrr@tolkien.com');
            INSERT OR IGNORE INTO Person (name, email) VALUES ('Christopher Tolkien','chris@tolkien.com');
            INSERT OR IGNORE INTO Person (name, email) VALUES ('Marc André Meyers','marc.meyers@biomaterials.com')
            INSERT OR IGNORE INTO Person (name, email) VALUES ('Po-Yu Chen','po-yu.chen@biomaterials.com')
            ''')

cur.close()
conn.close()