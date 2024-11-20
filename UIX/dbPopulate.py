import sqlite3

conn = sqlite3.connect('slot_machines.db')
cursor = conn.cursor()

with open('static/js/db.sql', 'r') as f:
    sql = f.read()

try:
    cursor.executescript(sql)
    conn.commit()
    print("Database populated successfully")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    cursor.close()
    conn.close()