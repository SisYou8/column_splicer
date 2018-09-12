import os
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.run(debug=True)
app.config['DEBUG'] = True

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/doc/<int:doc_id>')
def show_user_profile(doc_id):
    return render_template('doc.html', doc_id=doc_id)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file1' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file1']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file1.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file1:
            filename = secure_filename(file.filename)
            file.save(os.path.join("./uploads/", filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('upload.html')

@app.route('/uploaded_file/<filename>')
def uploaded_file(filename):
    return "congrats"
