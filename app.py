import json
from flask import Flask, request, jsonify
import sqlite3
from author_helper import *
from book_helper import *

app = Flask(__name__)

def create_book_author_database(database_name = 'library.db'):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            genre TEXT,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors (id)
        )
    """)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # create_book_author_database("library.db")
    app.run(debug=True)
