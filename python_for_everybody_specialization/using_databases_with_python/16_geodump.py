import sqlite3
import json
import codecs

conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
handle = codecs.open('where.js', 'w', 'utf-8')
handle.write('myData = [\n')
count = 0

for row in cur:
    data = str(row[1].decode())
    try: js = json.loads(str(data))
    except: continue

    if len(js['features']) == 0: continue

    try:
        lat = js['features'][0]['geometry']['coordinates'][1]
        lon = js['features'][0]['geometry']['coordinates'][0]
        where = js['features'][0]['properties']['display_name']
        where = where.replace("'", "")
    except:
        print('Unexpected format')
        print(js)

    try:
        print(where, lat, lon)
        count += 1
        if count > 1 : handle.write(",\n")
        output = "["+str(lat)+","+str(lon)+", '"+where+"']"
        handle.write(output)
    except: pass

