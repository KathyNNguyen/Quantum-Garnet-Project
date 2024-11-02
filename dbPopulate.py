import sqlite3

conn = sqlite3.connect('slot_machines.db')
cursor = conn.cursor()

with open('db.sql', 'r') as f:
    sql = f.read()
    
cursor.executescript(sql)

conn.commit()
cursor.close()
conn.close()