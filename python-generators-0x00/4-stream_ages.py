from seed import connect_to_prodev


def stream_user_ages():
    connection = None
    cursor = None
    try:
        connection = connect_to_prodev()
        cursor = connection.cursor(dictionary=True)
        # offset = 0
        cursor.execute(f"SELECT age FROM user_data;")
        user = cursor.fetchone()

        while user:
            yield user["age"]
            user = cursor.fetchone()

    finally:
        if cursor != None:
            cursor.close()
        if connection != None:
            connection.close()


def calculate_average_age():
    total_age = 0
    users = 0
    user_ages = stream_user_ages()

    for age in user_ages:
        total_age += age
        users += 1

    return total_age / users if users > 0 else 0
