from flask import render_template
from app import app

# Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Register Page
@app.route('/register')
def register():
    return render_template('register.html')