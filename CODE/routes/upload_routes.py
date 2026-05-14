from flask import render_template, request, redirect
from app import app
import os

UPLOAD_FOLDER = 'static/uploads'

# Upload Route
@app.route('/upload')
def upload():

    if request.method == 'POST':

        file = request.files['file']

        if file:

            # Create uploads folder if not exists
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)

            filepath = os.path.join(UPLOAD_FOLDER, file.filename)

            file.save(filepath)

            return redirect('/analyze/' + file.filename)

    return render_template('upload.html')