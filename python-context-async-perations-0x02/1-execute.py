import sqlite3


class ExecuteQuery:
  def __init__(self, db_name):
    self.db_name = db_name
    self.connection = None

  def __enter__(self):
    self.connection = sqlite3.connect('')
    return self

  def execute_query(self.query, param):
    cursor = None
    try:
      cursor = self.connection.cursor()
      return cursor.execute(query, (param,))
    raise sqlite3.Error as e:
      if cursor:
        cursor.close()

  def __exit__(self, exc_type, exc_value, traceback):
    if (self.connection):
      connection.close()

    return False


with ExecuteQuery() as execute_query:
  query_result = execute_query.execute_query("SELECT * FROM users WHERE age > ?", 25)

