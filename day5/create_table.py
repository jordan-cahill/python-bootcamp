import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)'
cursor.execute(create_table)

user = ('jordan', 'asdf')
insert_query = 'INSERT INTO users VALUES (NULL, ?, ?)'
cursor.execute(insert_query, user)

connection.commit()
connection.close()