'''Syntax of operating mysql is quite like the sqlite3 one.
the wild card is % in sql statement of mysql'''
import mysql.connector

con = mysql.connector.connect(user='root', password='newpass', database='student', use_unicode=True)
cursor = con.cursor()
res = cursor.execute()
