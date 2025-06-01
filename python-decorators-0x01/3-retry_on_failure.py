import time
import sqlite3
import functools


def with_db_connection(func):
  def wrapper(*args, **kwargs):
    connection = sqlite3.connect('users.db')

    try:
      return_val = func(connection, *args, **kwargs)
      return return_val
    finally:
      connection.close()

  return wrapper


def retry_on_failure(retries, delay):
  def decorator(func):
    def wrapper(*args, **kwargs):
      for i in range(retries):
        try:
          return_value = func(*args, **kwargs)
          return return_value
        except sqlite3.Error as e:
          time.sleep(delay)
      raise Exception(f"All {retries} retries failed.")
    return wrapper

  return decorator



@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM users")
  return cursor.fetchall()

users = fetch_users_with_retry()
print(users)