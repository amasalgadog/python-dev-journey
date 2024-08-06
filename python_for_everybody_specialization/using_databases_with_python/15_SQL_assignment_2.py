'''

Counting Organizations

This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)

When you have run the program on mbox.txt upload the resulting database file above for grading.
If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.

'''

import sqlite3
import re

handle = open('python_for_everybody_specialization/using_databases_with_python/mbox.txt')

conn = sqlite3.connect('15assignment.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

for item in handle:
    line = item.rstrip()

    if not re.search('^From:', line): continue

    data = re.findall('^From: \S+@(\S+)', line)
    org = data[0]

    cur.execute('SELECT count FROM Counts WHERE org=?', (org,))

    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?,1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org=?', (org,))

conn.commit()

query = 'SELECT org,count FROM Counts ORDER BY count DESC'
for row in cur.execute(query):
    print(row[0], row[1])

cur.close()
