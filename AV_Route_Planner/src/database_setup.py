import sqlite3
from sqlite3 import Connection


def create_db():
    try:
        conn = sqlite3.connect('data/routes.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS routes (id INTEGER PRIMARY KEY, 
                origin TEXT NOT NULL, destination TEXT NOT NULL, route_data TEXT, created_at
                DATETIME DEFAULT CURRENT_TIMESTAMP)''')

        conn.commit()
        print("Table 'routes created successfully!")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

    if __name__ == "__main__":
        create_db()