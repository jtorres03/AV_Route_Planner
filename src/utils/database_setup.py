import sqlite3
import os

def create_db():
    try:
        # Ensure the 'data' folder exists
        os.makedirs('data', exist_ok=True)

        # Connect to the database
        conn = sqlite3.connect('data/routes.db')
        c = conn.cursor()

        # Create the table
        c.execute('''CREATE TABLE IF NOT EXISTS routes (
            id INTEGER PRIMARY KEY, 
            origin TEXT NOT NULL, 
            destination TEXT NOT NULL, 
            route_data TEXT, 
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP)''')

        conn.commit()
        print("Table 'routes' created successfully!")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection only if it was successfully created
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    create_db()
