import sqlite3

def create_db():
    conn = sqlite3.connect('data/routes.db')