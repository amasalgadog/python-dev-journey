import sqlite3
import re

database = 'python_for_everybody_specialization/using_databases_with_python/emaildb.sqlite'
# this will create a new database if it doesn't exists
conn = sqlite3.connect(database)
cur = conn.cursor()
# database cursor is a control structure that enables traversal over the records in a database and it's created with .cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
# drop table if already exists

cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')
# create new table called 'Counts' with email=TEXT and count=INTEGER (attritute=type)

handle = open('python_for_everybody_specialization/using_databases_with_python/mbox-short.txt')

# handle the file using regular expressions
for item in handle:

    line = item.rstrip()

    if not re.search('^From:', line):
        continue

    data = re.findall('^From: (\S+@\S+)', line)
    # data is a list so if we need one element, it must be called
    email = data[0]

    # question sign (?) is a placeholder a must be accompanied by a tuple after the string where it's placed
    # the tuple needs to have the variable holding the value
    cur.execute('SELECT count FROM Counts WHERE email =?', (email,))
    # cur.execute() data live temporarily in 'cur'

    row = cur.fetchone()
    # cur.fetchone() -> temporarily data in 'cur' will be stored in 'row' variable

    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?,1)', (email,))
        # create first row if there is none
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE email=?', (email,))
        # update 'count' value if 'email' already exists

    conn.commit()
    # .commit() will "publish" the database into the disk. It's a slow process
    
# order the database by descendent 'count' values and print them
sqlstr = 'SELECT email,count FROM Counts ORDER BY count DESC'
for row in cur.execute(sqlstr):
    print(row[0], row[1])
