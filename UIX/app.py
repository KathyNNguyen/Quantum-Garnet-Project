from flask import Flask, render_template, request, session, flash, redirect, url_for, jsonify
import sqlite3 as sql
import os
import secrets

# Create Flask instance.
app = Flask(__name__)
# Set a secret key for sessions.
app.secret_key = secrets.token_hex(16)
# Define the new database file.
user_accounts_db = 'UIX/user_accounts.db'
promotions_db = 'UIX/promotions.db'


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
            with sql.connect(user_accounts_db) as con:
                cur = con.cursor()
                # Update the query to include security_level
                cur.execute("SELECT first_name, last_name, email, date_of_birth, reward_balance, promotion_tier, security_level FROM user_accounts WHERE username = ?", (username,))
                user = cur.fetchone()
                
                if user:
                    # Pass the security_level along with other user data
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

    
@app.route('/admin')
def admin():
    if 'logged_in' in session:
        username = session['name']
        try:
            with sql.connect(user_accounts_db) as con:
                cur = con.cursor()
                cur.execute("SELECT security_level FROM user_accounts WHERE username = ?", (username,))
                result = cur.fetchone()
                
                if result and result[0] == 9:
                    return render_template('admin.html')
                else:
                    flash('Access denied: Admins only', 'danger')
                    return redirect(url_for('home'))
        except sql.Error as e:
            flash(f"Database error: {e}", 'danger')
            return redirect(url_for('home'))
    else:
        flash('You must be logged in to access this page', 'warning')
        return redirect(url_for('login'))

@app.route('/big-winners')
def big_winners():
    return render_template('big-winners.html')

@app.route('/create-account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        date_of_birth = request.form['date_of_birth']
        username = request.form['username']
        password = request.form['password']

        try:
            with sql.connect(user_accounts_db) as con:
                cur = con.cursor()

                cur.execute("SELECT MAX(account_num) FROM user_accounts")
                max_account_num = cur.fetchone()[0]
                if max_account_num is None:
                    account_num = 1000001
                else:
                    account_num = max_account_num + 1

                password_hash = password

                reward_balance = 0
                security_level = 1

                cur.execute("""
                    INSERT INTO user_accounts (account_num, username, password_hash, first_name, last_name, email, date_of_birth, reward_balance, security_level)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (account_num, username, password_hash, first_name, last_name, email, date_of_birth, reward_balance, security_level))

                con.commit()
                flash('Account created successfully!', 'success')
                return redirect(url_for('login'))

        except sql.Error as e:
            flash(f"Database error: {e}", 'danger')
            return redirect(url_for('create_account'))

    return render_template('create-account.html')


@app.route('/create-promotion', methods=['GET', 'POST'])
def create_promotion():
    if 'logged_in' in session:
        username = session['name']
        try:
            with sql.connect(user_accounts_db) as con:
                cur = con.cursor()
                # Retrieve the user's security level
                cur.execute("SELECT security_level FROM user_accounts WHERE username = ?", (username,))
                result = cur.fetchone()

                if result and result[0] == 9:  # Check if security_level is 9
                    if request.method == 'POST':
                        promotion_tier = request.form['promotion_tier']
                        promotion_name = request.form['promotion_name']
                        reward_value = request.form['reward_value']

                        try:
                            with sql.connect(promotions_db) as con:
                                cur = con.cursor()

                                cur.execute("SELECT MAX(promotion_id) FROM promotions")
                                max_promotion_id = cur.fetchone()[0]
                                if max_promotion_id is None:
                                    promotion_id = 1001
                                else:
                                    promotion_id = max_promotion_id + 1

                                cur.execute("""
                                    INSERT INTO promotions (promotion_id, promotion_tier, promotion_name, reward_value)
                                    VALUES (?, ?, ?, ?)
                                """, (promotion_id, promotion_tier, promotion_name, reward_value))

                                con.commit()
                                flash('Promotion created successfully!', 'success')
                                return redirect(url_for('admin'))  # Redirect to the admin page or another suitable page

                        except sql.Error as e:
                            flash(f"Database error: {e}", 'danger')
                            return redirect(url_for('create_promotion'))  # Redirect back to the form if there was an error

                    return render_template('create-promotion.html')  # Render the create-promotion.html template
                else:
                    flash('Access denied: Admins only', 'danger')
                    return redirect(url_for('home'))  # Redirect non-admin users to the home page

        except sql.Error as e:
            flash(f"Database error: {e}", 'danger')
            return redirect(url_for('home'))  # Redirect to the home page in case of an error

    else:
        flash('You must be logged in to access this page', 'warning')
        return redirect(url_for('login'))  # Redirect unauthenticated users to the login page


@app.route('/directory')
def directory():
    return render_template('directory.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            with sql.connect(user_accounts_db) as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM user_accounts WHERE username = ?", (username,))
                user = cur.fetchone()

                if user and user[2] == password:
                    session['logged_in'] = True
                    session['name'] = user[1]
                    session['security_level'] = user[9]
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
    if request.method == 'POST':
        session.pop('logged_in', None)
        session.pop('name', None)
        session.pop('SecurityLevel', None)
        flash('You have been logged out.', 'success')
        return redirect(url_for('login'))

    return redirect(url_for('login')) 

@app.route('/promotions')
def promotions():
    if 'logged_in' in session:
        username = session['name']
        try:
            with sql.connect(user_accounts_db) as con_user:
                cur_user = con_user.cursor()
                cur_user.execute("SELECT reward_balance, promotion_tier FROM user_accounts WHERE username = ?", (username,))
                user = cur_user.fetchone()
                
                if user:
                    user_reward_balance = user[0]
                    user_promotion_tier = user[1]

                    with sql.connect(promotions_db) as con_promotions:
                        cur_promotions = con_promotions.cursor()
                        cur_promotions.execute("SELECT promotion_name, reward_value FROM promotions WHERE promotion_tier = ?", (user_promotion_tier,))
                        promotions = cur_promotions.fetchall()

                        if promotions:
                            promotion_data = [{'promotion_name': name, 'reward_value': value} for name, value in promotions]
                        else:
                            flash('No promotions found for this user', 'danger')
                            return redirect(url_for('home'))
                        
                    return render_template('promotions.html', user_reward_balance=user_reward_balance, user_promotion_tier=user_promotion_tier, promotion_data=promotion_data)
                else:
                    flash('No promotions found for this user', 'danger')
                    return redirect(url_for('home'))
                
        except sql.Error as e:
            flash(f"Database error: {e}", 'danger')
            return redirect(url_for('home'))
    else:
        flash('You must be logged in to view promotions', 'warning')
        return redirect(url_for('login'))


@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

@app.route('/api/slot-machines')
def get_slot_machines():
    connection = sqlite3.connect('db.sql')
    cursor = connection.cursor()

    query = """
        SELECT 
            machine_id, name, availability, average_session, 
            location, location_features, game_theme, game_type, 
            game_features, maximum_bet, minimum_bet, rtp, reward_program,
            top, left
        FROM slot_machines
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    # Map results to JSON format
    machines = [
        {
            "machine_id": row[0],
            "name": row[1],
            "availability": row[2],
            "average_session": row[3],
            "location": row[4],
            "location_features": row[5],
            "game_theme": row[6],
            "game_type": row[7],
            "game_features": row[8],
            "maximum_bet": row[9],
            "minimum_bet": row[10],
            "rtp": row[11],
            "reward_program": row[12],
            "top": row[13],
            "left": row[14],
        }
        for row in rows
    ]

    connection.close()
    return jsonify(machines)

@app.route('/slot-map')
def slot_map():
    return render_template('slot-map.html')


if __name__ == '__main__':
    app.run(debug=True)
