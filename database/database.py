import sqlite3
import os

# Folder containing database.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Full path to bank.db
DB_PATH = os.path.join(BASE_DIR, "bank.db")

connection = sqlite3.connect(DB_PATH)

print("Database Connected Successfully!")

connection.close()