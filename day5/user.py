import sqlite3

class User:

    def __init__(self, id_, username, password):
        self.id = id_
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE username=?'
        result = cursor.execute(query, (username,))
        row = result.fetchone()

        if row:
            #user = cls(row[0], row[1], row[2])
            user = cls(*row)    # we are doing *args into a required positional function
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE id=?'
        result = cursor.execute(query, (id,))
        row = result.fetchone()

        if row:
            #user = cls(row[0], row[1], row[2])
            user = cls(*row)    # we are doing *args into a required positional function
        else:
            user = None

        connection.close()
        return user