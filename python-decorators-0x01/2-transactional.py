import sqlite3 
import functools

def transactional(func):
  def wrapper(*args, **kwargs):
    if (args):
      connection = args[0]
      try:
        return_val = func(*args, **kwargs)
        connection.commit()
        return return_val
      except sqlite3.Error as e:
        connection.rollback()
        raise
    else:
      return func(*args, **kwargs)
    
  return wrapper


def with_db_connection(func):
  def wrapper(*args, **kwargs):
    connection = sqlite3.connect('users.db')

    try:
      return_val = func(connection, *args, **kwargs)
      return return_val
    finally:
      connection.close()

  return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
  cursor = conn.cursor()
  cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
  #### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')