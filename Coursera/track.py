import xml.etree.ElementTree as ET
import sqlite3

database = 'itunes-trackdb.sqlite'
conn = sqlite3.connect(database)
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    artist_id INTEGER UNIQUE,
    title INTEGER UNIQUE
);

CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE,
    album_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)
;''')

fname = input('Enter file name: ')
if(len(fname) < 1): fname = 'Library.xml'

def matchkey(d, key):
    '''
    Match the key, and fetch the value:
    The frist argument d's structure looks like
    child: <key>keyshere</key>
    child.next: <string>IamWhatYouWant!LeaveThatGirl!</string>.
    First match the key, second go to the next child and then fetch the text.
    Remember, the key and value in xml files are all child with no difference.
    You should get the tag and judge whether it is key or value by yourself.
    Brilliant one!
    '''
    found = False
    for child in d:
        # second go to the next child and fetch the text
        if found: return child.text
        # first find the key
        if child.tag == 'key' and child.text == key:
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('All the tracks counts:', len(all))
for entry in all:
    # if the entry is not a Track formatted data, continue
    if(matchkey(entry, 'Track ID') is None): continue

    name = matchkey(entry, 'Name')
    artist = matchkey(entry, 'Artist')
    album = matchkey(entry, 'Album')
    count = matchkey(entry, 'Play Count')
    rating = matchkey(entry, 'Rating')
    length = matchkey(entry, 'Total Time')

    # if the one of them is none, do not do the sql things.
    if name is None or artist is None or album is None:
        continue

    # print(name, artist, album, count, rating, length)
    print(album)

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
            values (?)''', (artist,))
    cur.execute('SELECT id from Artist where name = (?)', (artist,))
    # fetchone() returns a list length one
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (artist_id, title)
            values (?, ?)''', (artist_id, album))
    cur.execute('SELECT id from Album where title = ?', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, len, rating, count)
            VALUES (?, ?, ?, ?, ?)''',
            (name, album_id, length, rating, count))

    conn.commit()

cur.close()
conn.close()

