import json
import sqlite3

class Member():
    def __init__(self, name, title, role, course_id=-1, user_id=-1):
        self.name = name
        self.title = title
        self.role = role
        self._course_id = course_id
        self._user_id = user_id

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, course_id):
        self._course_id = course_id

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id


if __name__ == '__main__':
    conn = sqlite3.connect('roster_data.sqlite')
    cur = conn.cursor()
    sql_script = '''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;

    CREATE TABLE User(
        id INTEGER PRIMARY KEY NOT NULL,
        name TEXT
    );

    CREATE TABLE Course(
        id INTEGER PRIMARY KEY NOT NULL,
        title TEXT
    );

    CREATE TABLE Member(
        user_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY(user_id, course_id)
    )

    '''

    cur.executescript(sql_script)

    filename = input('load json filenameiles:')
    if len(filename) < 1:
        filename = 'roster_data_sample.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

# read data from json
    with open('roster_data_sample.json', 'r') as f:
        content = f.read()
    stuffs = json.loads(content)

# retrieve the data build Member and insert to the database and commmit connection
    for each in stuffs:
        try:
            member = Member(each[0], each[1], each[2])
        except IndexError:
            print('Could not build member')
            pass

        cur.execute('''INSERT INTO User (name)
                VALUES ( ? )''', (member.name,))
        member.user_id = cur.execute('''SELECT id FROM User
                WHERE name = ?''', (member.name,)).fetchone()[0]

        cur.execute('''INSERT INTO Course (title)
                VALUES (?)''', (member.title,))
        member.course_id = cur.execute('''SELECT id FROM Course
                WHERE title = ?''', (member.title,)).fetchone()[0]

        cur.execute('''INSERT INTO Member (user_id, course_id)
                       VALUES (?, ?)''', (member.user_id, member.course_id))

        conn.commit()



















