import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS clients (
        id SERIAL PRIMARY KEY,
        user_id BIGINT,
        name TEXT,
        phone TEXT,
        service TEXT,
        date TEXT,
        time TEXT
    )
    """
)

conn.commit()


def save_client(
    user_id,
    name,
    phone,
    service,
    date,
    time
):

    cursor.execute(
        """
        INSERT INTO clients
        (user_id, name, phone, service, date, time)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id
        """,
        (
            user_id,
            name,
            phone,
            service,
            date,
            time
        )
    )

    client_id = cursor.fetchone()[0]

    conn.commit()

    return client_id


def get_user_bookings(user_id):

    cursor.execute(
        """
        SELECT * FROM clients
        WHERE user_id = %s
        """,
        (user_id,)
    )

    return cursor.fetchall()


def is_time_taken(date, time):

    cursor.execute(
        """
        SELECT * FROM clients
        WHERE date = %s AND time = %s
        """,
        (date, time)
    )

    booking = cursor.fetchone()

    return booking is not None


def delete_client(client_id):

    cursor.execute(
        """
        DELETE FROM clients
        WHERE id = %s
        """,
        (client_id,)
    )

    conn.commit()

def get_clients():

    cursor.execute(
        "SELECT * FROM clients"
    )

    return cursor.fetchall()    


def get_total_bookings():

    cursor.execute(
        "SELECT COUNT(*) FROM clients"
    )

    return cursor.fetchone()[0]


def get_bookings_by_date(date):

    cursor.execute(
        """
        SELECT * FROM clients
        WHERE date = %s
        """,
        (date,)
    )

    return cursor.fetchall()



def get_all_bookings():

    cursor.execute(
        "SELECT * FROM clients"
    )

    return cursor.fetchall()


def get_bookings_count_by_date(date):

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM clients
        WHERE date = %s
        """,
        (date,)
    )

    return cursor.fetchone()[0]