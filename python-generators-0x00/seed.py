from os import getenv
from mysql.connector import Error, connect, MySQLConnection

# use reader for getting each row as list of strings, use DictReader to get each row as dictionaries if column names exist
from csv import DictReader, reader


def main():
    connection = None
    cursor = None

    try:
        with open("../user_data.csv", mode="r", newline="", encoding="utf-8") as file:
            reader = DictReader(file)

            for row in reader:
                print(row)

        # simpler implementation of instantiating MySQLConnection then calling connect on it
        connection: MySQLConnection = connect(
            host="localhost",
            user="root",
            # getting environment variable from the os env
            # set using export MYSQL_PASSWORD='my-mysql-password'
            password=getenv("MYSQL_PASSWORD"),
            database="ALX_prodev",
        )

        cursor = connection.cursor()
        cursor.execute("SHOW TABLES;")

        # TODO: explore other methods we can call on cursor
        for table in cursor.fetchall():
            print(table)

    except Error as e:
        print(f"Error: {e}")

    finally:
        # closing the cursor is "best practice" as per the glorious chatgpt
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


def read_csv(file_name: str):
    with open(file_name, mode="r", newline=None, encoding="utf-8") as file:
        reader = DictReader(file)

        if not reader.fieldnames:
            raise ValueError("CSV file is missing header row (column names).")

        data = []

        for row_num, row in enumerate(reader, start=2):
            if None in row.values():
                raise ValueError(f"Missing data in row {row_num}: {row}")
            data.append(row)

        return data

    return data


def connect_db() -> MySQLConnection:
    connection = None

    try:
        connection = connect(
            host="localhost",
            user="root",
            password=getenv("MYSQL_PASSWORD"),
            # database="ALX_prodev",
        )

        if connection.is_connected():
            return connection
        else:
            raise Error("Error connecting to db")

    except Error as e:
        if connection != None:
            connection.close()
        print(f"Error: {e}")


def create_database(connection: MySQLConnection):
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""CREATE DATABASE IF NOT EXISTS ALX_prodev;""")
    finally:
        if cursor != None:
            cursor.close()


def connect_to_prodev():
    connection = None

    try:
        connection = connect(
            host="localhost",
            user="root",
            password=getenv("MYSQL_PASSWORD"),
            database="ALX_prodev",
        )

        if connection.is_connected():
            return connection
        else:
            raise Error("Error connecting to db")

    except Error as e:
        if connection != None:
            connection.close()
        print(f"Error: {e}")


def create_table(connection: MySQLConnection):
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS user_data (
                      user_id VARCHAR(255) PRIMARY KEY DEFAULT (UUID()),
                      name VARCHAR(255) NOT NULL,
                      email VARCHAR(255) NOT NULL,
                      age DECIMAL(5, 2) NOT NULL
                   );"""
        )
    finally:
        if cursor != None:
            cursor.close()


def table_has_data(connection: MySQLConnection, table_name: str):
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")

        return cursor.fetchone()[0] > 0
    finally:
        if cursor != None:
            cursor.close()


# def insert_data(connection: MySQLConnection, data: list[dict[str, str]]):
def insert_data(connection: MySQLConnection, data: str):
    if table_has_data(connection, "user_data"):
        return

    cursor = None
    try:
        cursor = connection.cursor()
        data = read_csv(data)
        query = """
        INSERT INTO user_data (name, email, age)
        VALUES (%s, %s, %s)
        """

        for row in data:
            row_values = (row["name"], row["email"], int(row["age"]))
            cursor.execute(query, row_values)

        connection.commit()

    finally:
        if cursor != None:
            cursor.close()


if __name__ == "__main__":
    # main()
    data = read_csv("../user_data.csv")
    for row in data:
        print(row)
