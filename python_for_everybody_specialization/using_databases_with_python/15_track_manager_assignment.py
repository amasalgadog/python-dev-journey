'''

Musical Track Database

This application will read an iTunes export file in CSV format and produce a properly normalized database with this structure:

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);

If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/tracks.zip. 
The ZIP file contains the tracks.csv file to be used for this assignment. 
You can export your own tracks from iTunes and create a database, but for the database that you turn in for this assignment, only use the tracks.csv data that is provided. You can adapt the tracks_csv.py application in the zip file to complete the assignment.

To grade this assignment, the program will run a query like this on your uploaded database and look for the data it expects to see:

SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3

The expected result of the modified query on your database is: (shown here as a simple HTML table with titles)

Track	Artist	Album	Genre
Chase the Ace	AC/DC	Who Made Who	Rock
D.T.	AC/DC	Who Made Who	Rock
For Those About To Rock (We Salute You)	AC/DC	Who Made Who	Rock

'''

import sqlite3

conn = sqlite3.connect('15manager.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Track')
cur.execute('''
            CREATE TABLE Track (
            id INTEGER NOT NULL, 
            title TEXT, 
            rating INTEGER, 
            len INTEGER, 
            count INTEGER, 
            album_id INTEGER,
            genre_id INTEGER,
            FOREIGN KEY (album_id) REFERENCES Album (id), 
            FOREIGN KEY (genre_id) REFERENCES Genre (id), 
            PRIMARY KEY (id AUTOINCREMENT)
            )''')

cur.execute('DROP TABLE IF EXISTS Album')
cur.execute('''
            CREATE TABLE Album (
            id INTEGER NOT NULL,
            title TEXT UNIQUE,
            artist_id INTEGER NOT NULL,
            FOREIGN KEY (artist_id) REFERENCES Artist (id),
            PRIMARY KEY (id)
            )''')

cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('''
            CREATE TABLE Artist (
            id INTEGER NOT NULL, 
            name TEXT UNIQUE, 
            PRIMARY KEY(id)
            )''')

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

    cur.execute("INSERT OR IGNORE INTO Genre (name) VALUES ( ?)", (genre,))
    cur.execute("SELECT id FROM Genre WHERE name=?", (genre, ))
    genre_id = cur.fetchone()[0]
    
    cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES ( ?)", (artist,))
    cur.execute("SELECT id FROM Artist WHERE name=?", (artist,))
    artist_id = cur.fetchone()[0]
    
    cur.execute("INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ?)", (album,artist_id,))
    cur.execute("SELECT id FROM Album WHERE title=?", (album, ))
    album_id = cur.fetchone()[0]

    cur.execute("INSERT OR REPLACE INTO Track (title, rating, len, count, album_id, genre_id) VALUES ( ?, ?, ?, ?, ?, ?)", (track, rating, length, count, album_id, genre_id))

    conn.commit()

cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name 
            FROM Track JOIN Genre JOIN Album JOIN Artist ON Track.genre_id = Genre.id and Track.album_id = Album.id AND Album.artist_id = Artist.id
            ORDER BY Artist.name ASC, Track.title ASC LIMIT 3
            ''')
# in order to get the SAME expected result, the table returned from the query must be FIRST order by artist name (asc) and THEN it must be order by track title (asc)

result = cur.fetchall()

for item in result:
    print(item)

cur.close()

conn.close()