import sqlite3

conn = sqlite3.connect("barbershop.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    service TEXT,
    time TEXT
)
""")

conn.commit()

def save_client(name, phone, service, time):

    cursor.execute(
        "INSERT INTO clients (name, phone, service, time) VALUES (?, ?, ?, ?)",
        (name, phone, service, time)
    )

    conn.commit()

    return cursor.lastrowid

def get_clients():
    cursor.execute("SELECT * FROM clients")
    return cursor.fetchall()

def delete_client(client_id):

    cursor.execute(
        "DELETE FROM clients WHERE id = ?",
        (client_id,)
    )

    conn.commit()