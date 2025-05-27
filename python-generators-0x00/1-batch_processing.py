from seed import connect_to_prodev


def stream_users_in_batches(batch_size: int):
    connection = None
    cursor = None

    try:
        connection = connect_to_prodev()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        streamed_users = cursor.fetchmany(batch_size)
        while streamed_users:
            yield streamed_users
            streamed_users = cursor.fetchmany(batch_size)
    finally:
        cursor.close()
        connection.close()


def batch_processing(batch_size: int):
    # ! Removed because it generates new generators on every call
    # batch = next(stream_users_in_batches(batch_size))
    # while batch:
    #     yield [user for user in batch if user["age"] > 25]
    #     batch = next(stream_users_in_batches(batch_size))

    # ? Fixed implementation
    for batch in stream_users_in_batches(batch_size):
        yield [user for user in batch if user["age"] > 25]

    return
