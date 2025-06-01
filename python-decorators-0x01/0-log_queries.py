import sqlite3
import functools
from datetime import datetime


def log_queries(func):
    def wrapper(*args, **kwargs):

        if (args):
            print(datetime.now())
            print(args[0])

        return func(*args, **kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")