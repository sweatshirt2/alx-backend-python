import time
import sqlite3 
import functools


query_cache = {}


def cache_query(func):

    def wrapper(*args, **kwargs):
        query = kwargs['query']
        if query in query_cache:
            return query_cache[query]
        result_val = func(*args, **kwargs)
        query_cache[query] = result_val

        return result_val
    return wrapper


def with_db_connection(func):
  def wrapper(*args, **kwargs):

      connection = sqlite3.connect('users.db')
      return_val = func(connection, *args, **kwargs)
      connection.close()
      return return_val

  return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")