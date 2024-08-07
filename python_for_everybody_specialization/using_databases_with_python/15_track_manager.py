'''

Exercise to simulate a track-managing database
UPDATE 0: create tables and insert data into them

'''

import sqlite3

# virtually create database
conn = sqlite3.connect('15manager.sqlite')
cur = conn.cursor()

# create or redo Track table
cur.execute('DROP TABLE IF EXISTS Track')
cur.execute('''
            CREATE TABLE Track (
            id INTEGER NOT NULL, 
            title TEXT NOT NULL, 
            rating INTEGER, 
            len INTEGER NOT NULL, 
            count INTEGER, 
            album_id INTEGER,
            genre_id INTEGER NOT NULL,
            FOREIGN KEY (album_id) REFERENCES Album (id), 
            FOREIGN KEY (genre_id) REFERENCES Genre (id), 
            PRIMARY KEY (id AUTOINCREMENT)
            )''')
# PRIMARY KEY (<attribute> AUTOINCREMENT) 
# declare <attribute> as an unique key that increase its number every time a record/value is added to the table

# FOREIGN KEY (<another_table_attribute>) REFERENCES <another_table> (<attribute>) 
# declare <another_table_attribute> as a link to said table's <attribute> in order to efficiently reference one table to another

# create or redo Album table
cur.execute('DROP TABLE IF EXISTS Album')
cur.execute('''
            CREATE TABLE Album (
            id INTEGER NOT NULL,
            title TEXT,
            artist_id INTEGER NOT NULL,
            FOREIGN KEY (artist_id) REFERENCES Artist (id),
            PRIMARY KEY (id AUTOINCREMENT)
            )''')

# create or redo Artist table
cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('''
            CREATE TABLE Artist (
            id INTEGER NOT NULL, 
            name TEXT, 
            PRIMARY KEY(id AUTOINCREMENT)
            )''')

# create or redo Genre table
cur.execute('DROP TABLE IF EXISTS Genre')
cur.execute('''
            CREATE TABLE Genre (
            id INTEGER NOT NULL,
            name TEXT NOT NULL,
            PRIMARY KEY (id AUTOINCREMENT)
            )''')

# insert record/data into Genre table
cur.execute("INSERT INTO Genre (name) VALUES ('Rock')")
cur.execute("INSERT INTO Genre (name) VALUES ('R&B')")
cur.execute("INSERT INTO Genre (name) VALUES ('Trance')")

# insert record/data into Artist table
cur.execute("INSERT INTO Artist (name) VALUES ('Bon Jovi')")
cur.execute("INSERT INTO Artist (name) VALUES ('Usher')")
cur.execute("INSERT INTO Artist (name) VALUES ('Armin van Buuren')")

# insert record/data into Album table           
cur.execute("INSERT INTO Album (title, artist_id) VALUES ('Forever', 1)")
cur.execute("INSERT INTO Album (title, artist_id) VALUES ('Coming Home', 2)")
cur.execute("INSERT INTO Album (title, artist_id) VALUES ('Mirage', 3)")

# store the virtual database tables phisically
conn.commit()

# insert record/data into Track table
cur.execute("INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('Coming Home', 5, 315, 0, 2, 2)")
cur.execute("INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('Good Good', 5, 407, 0, 2, 2)")
cur.execute("INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('Mirage', 5, 641, 0, 3, 3)") 
cur.execute("INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('This Light Between Us', 5, 509, 0, 3, 3)")
cur.execute("INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('TWe Made It Look Easy', 5, 315, 0, 1, 1)")
cur.execute("INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('Kiss The Bride', 5, 351, 0, 1, 1)")

# store the virtual database new data records physically
conn.commit()

# close cursor
cur.close()

# close connection
conn.close()