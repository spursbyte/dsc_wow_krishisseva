import os
from flask import Flask, render_template, request
import keras
from keras.models import load_model
import pickle
UPLOAD_FOLDER = '/static/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
@app.route('/')
def home_page():
    return render_template('index.html')
@app.route('/PLANT-DISEASE', methods=['GET', 'POST'])
def upload_page_plant_disease():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):

            
            model = load_model('plant_model.h5')
            text = model.predict(file)

            # extract the text and display it
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=text,
                                   img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

@app.route('/WEED-DETECTION', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
            # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
            # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):
            model = load_model('model.h5')
            text = model.predict(file)

                # extract the text and display it
            return render_template('upload.html',
                                    msg='Successfully processed',
                                    extracted_text=text,
                                    img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')
if __name__=='__main__':
    app.run()