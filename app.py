from flask import Flask, render_template, request, session, flash, redirect
from markupsafe import Markup
from flask_recaptcha import ReCaptcha
import sqlite3
import os
import nltk
import chatbot

# Downloading necessary NLTK packages (only needed once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

app = Flask(__name__)

# @app.context_processor
# def utility_processor():
#     from markupsafe import Markup
#     return dict(Markup=Markup)


# Set up ReCaptcha configuration
app.config.update(dict(
    RECAPTCHA_ENABLED=True,
    RECAPTCHA_SITE_KEY="6LdbAx0aAAAAAANl04WHtDbraFMufACHccHbn09L",
    RECAPTCHA_SECRET_KEY="6LdbAx0aAAAAAMmkgBKJ2Z9xsQjMD5YutoXC6Wee"
))
recaptcha = ReCaptcha(app=app)
app.secret_key = os.urandom(24)
app.static_folder = 'static'

# Initialize the SQLite database
DATABASE = 'register.db'

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # To return rows as dictionaries
    return conn

# Rest of the code...

def init_db():
    """Initializes the database and creates necessary tables if they don't exist."""
    conn = get_db_connection()
    cur = conn.cursor()

    # Create 'users' table if it doesn't exist
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )''')

    # Create 'suggestion' table if it doesn't exist
    cur.execute('''CREATE TABLE IF NOT EXISTS suggestion (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        message TEXT NOT NULL,
        FOREIGN KEY (email) REFERENCES users(email) ON DELETE CASCADE
    )''')

    conn.commit()
    conn.close()

# Initialize the database at startup
init_db()

@app.route('/')
def login():
    """Renders the login page."""
    return render_template("login.html")

@app.route('/index')
def home():
    """Renders the homepage if the user is logged in."""
    if 'id' in session:
        return render_template('index.html')
    else:
        flash('You must log in first.')
        return redirect('/')

@app.route('/register')
def register():
    """Renders the registration page."""
    return render_template('register.html')

@app.route('/forgot')
def forgot():
    """Renders the forgot password page."""
    return render_template('forgot.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    """Validates user login credentials."""
    email = request.form.get('email')
    password = request.form.get('password')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cur.fetchone()
    conn.close()

    if user:
        session['id'] = user['id']
        flash('You were successfully logged in')
        return redirect('/index')
    else:
        flash('Invalid credentials, please try again.')
        return redirect('/')

@app.route('/add_user', methods=['POST'])
def add_user():
    """Registers a new user and logs them in."""
    name = request.form.get('name')
    email = request.form.get('uemail')
    password = request.form.get('upassword')

    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        # Insert new user
        cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        session['id'] = cur.lastrowid  # Get the ID of the newly registered user
        flash('You have successfully registered!')
    except sqlite3.IntegrityError:
        flash('Email already registered! Please try a different email.')
    finally:
        conn.close()

    return redirect('/index')

@app.route('/suggestion', methods=['POST'])
def suggestion():
    """Stores user suggestions in the database."""
    email = request.form.get('uemail')
    suggesMess = request.form.get('message')

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO suggestion (email, message) VALUES (?, ?)", (email, suggesMess))
    conn.commit()
    conn.close()

    flash('Your suggestion has been successfully submitted!')
    return redirect('/index')

@app.route('/logout')
def logout():
    session.pop('id')
    return redirect('/')


@app.route("/get")
def get_bot_response():
    """Returns chatbot response to user input."""
    userText = request.args.get('msg')

    # Simple keyword matching for greetings and other responses
    if "hello" in userText.lower() or "hi" in userText.lower():
        bot_response = "Hello! How can I assist you today?"
    elif "how are you" in userText.lower():
        bot_response = "I'm good, thank you! How can I assist you today?"
    else:
        # Get response from the chatbot
        bot_response = str(chatbot.get_response(userText))

    return bot_response

if __name__ == "__main__":
    app.run(debug=True)
