from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/account')
def about():
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
