from flask import Flask, render_template, request, session, flash, redirect, url_for, jsonify
import sqlite3 as sql
import secrets

# Create Flask instance.
app = Flask(__name__)
# Set a secret key for sessions.
app.secret_key = secrets.token_hex(16)
# Define the database files.
user_accounts_db = 'UIX/user_accounts.db'
promotions_db = 'UIX/promotions.db'

# Route for home page.
@app.route('/')
def home():
    return render_template('home.html')

# Route for about page.
@app.route('/about')
def about():
    return render_template('about.html')

# Route for account page.
@app.route('/account')
def account():
    if 'logged_in' in session:
        username = session['name']
        try:
            # Connect to user_acount database.
            with sql.connect(user_accounts_db) as con:
                cur = con.cursor()
                cur.execute("SELECT first_name, last_name, email, date_of_birth, reward_balance, promotion_tier, security_level FROM user_accounts WHERE username = ?", (username,))
                user = cur.fetchone()
                
                if user:
                    # Render account page.
                    return render_template('account.html', user=user)
                else:
                    # Redirect to login if user not found.
                    flash('User not found', 'danger')
                    return redirect(url_for('login'))
        except sql.Error as e:
            flash(f"Database error: {e}", 'danger')
            return redirect(url_for('login'))
    else:
        flash('You must be logged in to view your account', 'warning')
        return redirect(url_for('login'))

# Route for admin page.   
@app.route('/admin')
def admin():
    if 'logged_in' in session:
        username = session['name']
        try:
            # Connect to user_account database.
            with sql.connect(user_accounts_db) as con:
                cur = con.cursor()
                cur.execute("SELECT security_level FROM user_accounts WHERE username = ?", (username,))
                result = cur.fetchone()
                
                # Checks if user is admin security_level.
                if result and result[0] == 9:
                    # Renders admin page.
                    return render_template('admin.html')
                else:
                    # Redirects home if not admin.
                    flash('Access denied: Admins only', 'danger')
                    return redirect(url_for('home'))
        except sql.Error as e:
            flash(f"Database error: {e}", 'danger')
            return redirect(url_for('home'))
    else:
        flash('You must be logged in to access this page', 'warning')
        return redirect(url_for('login'))

# Route for big-winners page.
@app.route('/big-winners')
def big_winners():
    return render_template('big-winners.html')

# Route for create-account page.
@app.route('/create-account', methods=['GET', 'POST'])
def create_account():
    if 'logged_in' in session:
        # Must be admin to create account when logged in.
        if session.get('security_level') == 9:
            # Collect form data for new account.
            if request.method == 'POST':
                first_name = request.form['first_name']
                last_name = request.form['last_name']
                email = request.form['email']
                date_of_birth = request.form['date_of_birth']
                username = request.form['username']
                password = request.form['password']

                try:
                    # Insert new account data.
                    with sql.connect(user_accounts_db) as con:
                        cur = con.cursor()

                        # Get next available account number.
                        cur.execute("SELECT MAX(account_num) FROM user_accounts")
                        max_account_num = cur.fetchone()[0]
                        if max_account_num is None:
                            account_num = 1000001
                        else:
                            account_num = max_account_num + 1
                        # Needs to be improved with real hashing.
                        password_hash = password

                        # Default reward_balance and security_level.
                        reward_balance = 0
                        security_level = 1 

                        cur.execute("""
                            INSERT INTO user_accounts (account_num, username, password_hash, first_name, last_name, email, date_of_birth, reward_balance, security_level)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, (account_num, username, password_hash, first_name, last_name, email, date_of_birth, reward_balance, security_level))

                        con.commit()
                        flash('Account created successfully!', 'success')
                        return redirect(url_for('home'))

                except sql.Error as e:
                    flash(f"Database error: {e}", 'danger')
                    return redirect(url_for('create_account'))

            return render_template('create-account.html') 

        else:
            flash('Access denied: Admins only', 'danger')
            return redirect(url_for('home')) 

    else:
        # If not logged in, any user can create account.
        if request.method == 'POST':
            # Collect form data for new account.
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            date_of_birth = request.form['date_of_birth']
            username = request.form['username']
            password = request.form['password']

            try:
                # Insert new account data.
                with sql.connect(user_accounts_db) as con:
                    cur = con.cursor()

                    # Get next available account number.
                    cur.execute("SELECT MAX(account_num) FROM user_accounts")
                    max_account_num = cur.fetchone()[0]
                    if max_account_num is None:
                        account_num = 1000001
                    else:
                        account_num = max_account_num + 1

                    # Needs to be improved with real hashing.
                    password_hash = password

                    # Default reward_balance and security_level.
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

        # Render create-account page.
        return render_template('create-account.html')

# Route to create-promotion (admin only).
@app.route('/create-promotion', methods=['GET', 'POST'])
def create_promotion():
    if 'logged_in' in session:
        username = session['name']
        try:
            # Connect to user_accounts database.
            with sql.connect(user_accounts_db) as con:
                cur = con.cursor()
                cur.execute("SELECT security_level FROM user_accounts WHERE username = ?", (username,))
                result = cur.fetchone()

                # Checks for admin. 
                if result and result[0] == 9:
                    if request.method == 'POST':
                        promotion_tier = request.form['promotion_tier']
                        promotion_name = request.form['promotion_name']
                        reward_value = request.form['reward_value']

                        try:
                            # Connects to promotions database.
                            with sql.connect(promotions_db) as con:
                                cur = con.cursor()

                                # Get next available promotion_id.
                                cur.execute("SELECT MAX(promotion_id) FROM promotions")
                                max_promotion_id = cur.fetchone()[0]
                                if max_promotion_id is None:
                                    promotion_id = 1001
                                else:
                                    promotion_id = max_promotion_id + 1

                                # Insert new promotion details.
                                cur.execute("""
                                    INSERT INTO promotions (promotion_id, promotion_tier, promotion_name, reward_value)
                                    VALUES (?, ?, ?, ?)
                                """, (promotion_id, promotion_tier, promotion_name, reward_value))

                                con.commit()
                                flash('Promotion created successfully!', 'success')
                                return redirect(url_for('admin'))

                        except sql.Error as e:
                            flash(f"Database error: {e}", 'danger')
                            return redirect(url_for('create_promotion'))

                    return render_template('create-promotion.html')
                else:
                    flash('Access denied: Admins only', 'danger')
                    return redirect(url_for('home')) 

        except sql.Error as e:
            flash(f"Database error: {e}", 'danger')
            return redirect(url_for('home'))

    else:
        flash('You must be logged in to access this page', 'warning')
        return redirect(url_for('login'))

# Route for directory page.
@app.route('/directory')
def directory():
    return render_template('directory.html')

# Route for login page.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            # Connect to user_accounts database.
            with sql.connect(user_accounts_db) as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM user_accounts WHERE username = ?", (username,))
                user = cur.fetchone()

                # Store session data once logged in.
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

# Route for logout functionality.
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        # Remove login values.
        session.pop('logged_in', None)
        session.pop('name', None)
        session.pop('SecurityLevel', None)
        flash('You have been logged out.', 'success')
        return redirect(url_for('login'))
    # Redirect to login page.
    return redirect(url_for('login')) 

# Route for promotions. 
@app.route('/promotions')
def promotions():
    # Checks if user is logged in.
    if 'logged_in' in session:
        username = session['name']
        try:
            # Connect to user_account database.
            with sql.connect(user_accounts_db) as con_user:
                cur_user = con_user.cursor()
                cur_user.execute("SELECT reward_balance, promotion_tier FROM user_accounts WHERE username = ?", (username,))
                user = cur_user.fetchone()
                
                # If user is found, get reward_balance and promotion_tier.
                if user:
                    user_reward_balance = user[0]
                    user_promotion_tier = user[1]

                    # Connect to promotions database.
                    with sql.connect(promotions_db) as con_promotions:
                        cur_promotions = con_promotions.cursor()
                        cur_promotions.execute("SELECT promotion_name, reward_value FROM promotions WHERE promotion_tier = ?", (user_promotion_tier,))
                        promotions = cur_promotions.fetchall()

                        # Promotion data based on tier.
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

# Route for rewards page.
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
