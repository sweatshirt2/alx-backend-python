import sqlite3
import functools

def with_db_connection(func):
  def wrapper(*args, **kwargs):

    if len(args) == 2:
      connection = sqlite.connect('users.db')
      return_val = func(*args, **kwargs, user_id)
      connection.close()
      return return_val
    
  return wrapper


@with_db_connection
def get_user_by_id(conn, user_id):
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
  return cursor.fetchone()


user = get_user_by_id(user_id=1)
print(user)