from seed import connect_to_prodev


def paginate_users(page_size, offset):
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazypaginate(page_size):
    offset = 0
    users = paginate_users(page_size, offset)
    while users:
        yield users
        offset += page_size
        users = paginate_users(offset)
