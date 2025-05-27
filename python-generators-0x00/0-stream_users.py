from seed import connect_to_prodev


def stream_users():
    connection = connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM user_data;")

    row = cursor.fetchone()

    while row:
        yield row
        row = cursor.fetchone()

    cursor.close()
