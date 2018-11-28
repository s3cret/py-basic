import sqlite3

# connect to SQLite database
# the db filename is "test.db"
# if the file doesn't exist, it will create one
db_file = 'test.db'
conn = sqlite3.connect(db_file)
# cusor in connection
cusor = conn.cursor()
# execute a sql statement to create table `student`
sql1 = 'create table user (id varchar(20) primary key, name varchar(20))'
cusor.execute(sql1)
sql2 = "insert into user (id, name) values ('1', 'Michael')"
cusor.execute(sql2)
# return the current cusor row count
print(cusor.rowcount)
cusor.close()
# commit the transaction
conn.commit()
# then you close a connection
conn.close()






