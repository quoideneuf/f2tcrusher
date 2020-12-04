from flask import Flask, render_template, request, redirect
import urllib.request
from werkzeug.utils import secure_filename
import os
import pdb
from .process import XLCrusher

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['xls', 'csv'])
UPLOAD_FOLDER = '/tmp'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home_view():
    return render_template('upload.html')
    # return "<h1>Welcome to the Matrix, Zachary</h1>"

@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            xlc = XLCrusher(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            products = xlc.process()
            return render_template("products.html", products = products)

            #return redirect('/')
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)
