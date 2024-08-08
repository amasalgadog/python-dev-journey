'''

Exercise to simulate a track-managing database
UPDATE 0: create tables and insert data into them
UPDATE 1: using join operator
UPDATE 2: add file with track records

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
            PRIMARY KEY (id)
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
            title TEXT UNIQUE,
            artist_id INTEGER NOT NULL,
            FOREIGN KEY (artist_id) REFERENCES Artist (id),
            PRIMARY KEY (id)
            )''')

# create or redo Artist table
cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('''
            CREATE TABLE Artist (
            id INTEGER NOT NULL, 
            name TEXT UNIQUE, 
            PRIMARY KEY(id)
            )''')

# create or redo Genre table
cur.execute('DROP TABLE IF EXISTS Genre')
cur.execute('''
            CREATE TABLE Genre (
            id INTEGER NOT NULL,
            name TEXT UNIQUE,
            PRIMARY KEY (id)
            )''')

handle = open('using_databases_with_python/tracks.csv')

for line in handle:
    line = line.strip()
    stuff = line.split(',')

    if len(stuff) < 6: continue

    track = stuff[0]
    artist = stuff[1]
    album = stuff[2]
    count = stuff[3]
    rating = stuff[4]
    length = stuff[5]
    genre = stuff[6]

    # IGNORE works with UNIQUE constraints, preventig a value from duplicating
    # if UNIQUE wasn't declared the query will just add the value again and the IGNORE operator will do nothing
    cur.execute("INSERT OR IGNORE INTO Genre (name) VALUES ( ?)", (genre,))
    cur.execute("SELECT id FROM Genre WHERE name=?", (genre, ))
    genre_id = cur.fetchone()[0]
    # because fetchone, fetchall and fetchmany return a list of data, an index must be given even if it's just one data
    
    cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES ( ?)", (artist,))
    cur.execute("SELECT id FROM Artist WHERE name=?", (artist,))
    artist_id = cur.fetchone()[0]
    
    cur.execute("INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ?)", (album,artist_id,))
    cur.execute("SELECT id FROM Album WHERE title=?", (album, ))
    album_id = cur.fetchone()[0]

    cur.execute("INSERT OR REPLACE INTO Track (title, rating, len, count, album_id, genre_id) VALUES ( ?, ?, ?, ?, ?, ?)", (track, rating, length, count, album_id, genre_id))

    conn.commit()


'''# insert record/data into Genre table
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

# print a relational table made by JOIN operator with Album title and Artist name
cur.execute("SELECT Album.title, Artist.name FROM Album JOIN Artist ON Album.artist_id=Artist.id")
result1 = cur.fetchall()
# print(result1)
# this print a list of tuples

# print a relational table made by JOIN operator with Track title, Album title and Artist name
# with more than 2 tables, there's need to be more JOIN operator, in this case Album linked both Track and Artist so it works perfectly for the FROM operator
cur.execute("SELECT Track.title, Album.title, Artist.name FROM Album JOIN Track ON Track.album_id=Album.id JOIN Artist ON Album.artist_id=Artist.id")
result2 = cur.fetchall()
# print(result2)
# this also print a list of tuples but this time with 3 values in each one

# print a relational table made by JOIN operator with Track title, Album title, Artist name and Genre
# this is another method for using more than 2 tables FROM <table1> JOIN <table2> JOIN <table3> JOIN ... <tablen> and then ON linking the respective tables plus AND operator between each relationship
cur.execute("SELECT Track.title, Album.title, Artist.name, Genre.name FROM Track JOIN Album JOIN Artist Join Genre ON Track.album_id=Album.id AND Album.artist_id=Artist.id AND Track.genre_id=Genre.id")
result3 = cur.fetchall()
# print(result3)
for item in result3:
    print(item)'''

# close cursor
cur.close()

# close connection
conn.close()