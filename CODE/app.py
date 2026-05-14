from flask import Flask, render_template, request, redirect
import os
import re

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Register Page
@app.route('/register')
def register():
    return render_template('register.html')

# Upload Route
@app.route('/upload', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':

        file = request.files['file']

        if file:

            # Create uploads folder
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)

            filepath = os.path.join(UPLOAD_FOLDER, file.filename)

            file.save(filepath)

            return redirect('/analyze/' + file.filename)

    return render_template('upload.html')

# Analyze Route
@app.route('/analyze/<filename>')
def analyze(filename):

    filepath = os.path.join(UPLOAD_FOLDER, filename)

    vulnerabilities = []

    try:

        with open(filepath, 'r', encoding='utf-8') as file:
            code = file.read()

        # Detect eval()
        if re.search(r'eval\(', code):

            vulnerabilities.append({
                'issue': 'Use of eval()',
                'severity': 'High',
                'recommendation': 'Avoid using eval()'
            })

        # Detect exec()
        if re.search(r'exec\(', code):

            vulnerabilities.append({
                'issue': 'Use of exec()',
                'severity': 'Critical',
                'recommendation': 'Avoid dynamic execution'
            })

        # Detect hardcoded password
        if 'password=' in code:

            vulnerabilities.append({
                'issue': 'Hardcoded Password',
                'severity': 'High',
                'recommendation': 'Use environment variables'
            })

    except Exception as e:

        return f"Error: {str(e)}"

    return render_template(
        'results.html',
        filename=filename,
        results=vulnerabilities
    )

# Run Flask
if __name__ == '__main__':
    app.run(debug=True)