from flask import Flask, render_template, request, session, flash, redirect, url_for
import sqlite3 as sql
import os
import secrets

# Create Flask instance.
app = Flask(__name__)
# Set a secret key for sessions.
app.secret_key = secrets.token_hex(16)
# Define the new database file.
db_file = 'UIX/user_accounts.sql'

# Check if the database file exists. If not, create and populate it.
if not os.path.exists(db_file):
    with open('user_accounts.sql', 'r') as sql_file:
        sql_script = sql_file.read()
    # Connect to the SQLite database (it will create the file if it doesn't exist).
    conn = sql.connect(db_file)
    c = conn.cursor()
    
    # Execute the SQL script to create the table and insert data.
    c.executescript(sql_script)
    
    # Commit and close the connection.
    conn.commit()
    conn.close()
    print("Database created and populated successfully.")
else:
    print("Database already exists.")


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/big-winners')
def big_winners():
    return render_template('big-winners.html')

@app.route('/create-account')
def create_account():
    return render_template('create-account.html')

@app.route('/directory')
def directory():
    return render_template('directory.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/promotions')
def promotions():
    return render_template('promotions.html')

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

@app.route('/slot-map')
def slot_map():
    return render_template('slot-map.html')


if __name__ == '__main__':
    app.run(debug=True)
