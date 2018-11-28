'''Note
You should close your cursor.
You should call connection.commit() to save the changed data.
You should close your connection to database;
The wild card is ? in sql statement of sqlite3.
'''
import sqlite3
con = sqlite3.connect('test.db')
cusor = con.cursor()
insert1 = "insert into user (id, name) values ('2', 'hack')"
select = "select * from user"
# cusor.execute(insert1)
cusor.execute(select)
results = cusor.fetchall()
cusor.close()
con.commit()
for each in results:
    print('Got one.')
    print('id is:', each[0])
    print('name is:', each[1])
