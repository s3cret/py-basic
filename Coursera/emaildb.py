import sqlite3

conn = sqlite3.connect('email.sqlite')
cur = conn.cursor()
# create table
cur.execute('drop table if exists emails')
cur.execute('''
create table emails (email text, counter integer)''')

filename = input('filename - ')
if(len(filename) < 1): filename = 'mbox-short.txt'
f = open(filename)

for line in f:
    counter = 0
    if not line.startswith('From'): continue
    pieces = line.split()
    email = pieces[1]
    counter += 1
    cur.execute('select counter from emails where email = ?', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO emails(email, counter)
values (?, 1)''', (email,))
    else:
        cur.execute('''UPDATE emails SET counter = counter + 1
WHERE email = ?''', (email,))
    conn.commit()

f.close()
cur.close()
conn.close()
