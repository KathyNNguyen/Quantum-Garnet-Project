from flask import Flask, render_template, request, session, flash, redirect, url_for
import sqlite3 as sql
import os
import secrets

# Create Flask instance.
app = Flask(__name__)
# Set a secret key for sessions.
app.secret_key = secrets.token_hex(16)
# Define the new database file.
db_file = 'UIX/user_accounts.db'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/account')
def account():
    if 'logged_in' in session:
        username = session['name']
        try:
            with sql.connect(db_file) as con:
                cur = con.cursor()
                cur.execute("SELECT first_name, last_name, email, date_of_birth, reward_balance FROM user_accounts WHERE username = ?", (username,))
                user = cur.fetchone()
                
                if user:
                    return render_template('account.html', user=user)
                else:
                    flash('User not found', 'danger')
                    return redirect(url_for('login'))
        except sql.Error as e:
            flash(f"Database error: {e}", 'danger')
            return redirect(url_for('login'))
    else:
        flash('You must be logged in to view your account', 'warning')
        return redirect(url_for('login'))

@app.route('/big-winners')
def big_winners():
    return render_template('big-winners.html')

@app.route('/create-account')
def create_account():
    return render_template('create-account.html')

@app.route('/directory')
def directory():
    return render_template('directory.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            with sql.connect(db_file) as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM user_accounts WHERE username = ?", (username,))
                user = cur.fetchone()

                if user and user[2] == password:
                    session['logged_in'] = True
                    session['name'] = user[1]
                    session['SecurityLevel'] = user[8]
                    flash('Login successful!', 'success')
                    return redirect(url_for('home'))
                else:
                    flash('Invalid username or password', 'danger')
        except sql.Error as e:
            flash(f"Database error: {e}", 'danger')
            return render_template('login.html')


    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # Handle POST request for logging out
    if request.method == 'POST':
        session.pop('logged_in', None)
        session.pop('name', None)
        session.pop('SecurityLevel', None)
        flash('You have been logged out.', 'success')
        return redirect(url_for('login'))

    return redirect(url_for('login')) 

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
