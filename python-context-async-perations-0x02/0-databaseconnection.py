import sqlite3


class DatabaseConnection:

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect("")
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            connection.close()

        return False


with DatabaseConnection("users") as connection:
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users;")
    except sqlite3.Error as e:
        if cursor:
            cursor.close()
