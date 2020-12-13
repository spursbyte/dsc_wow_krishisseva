import os
from flask import Flask, render_template, request,url_for,flash,redirect
import keras
from keras.models import load_model
import pickle
from keras.models import load_model
UPLOAD_FOLDER = '/static/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app = Flask(__name__)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def home_page():
    return render_template('index.html')
@app.route('/PLANT-DISEASE', methods=['GET', 'POST'])
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

            
            model = load_model('plant_model.h5')
            text = model.predict(file)

            # extract the text and display it
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=text,
                                   img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')
@app.route('/WEED-DETECTOR', methods=['GET', 'POST'])
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

@app.route('/advert')
def advert_page():
    return render_template('blog-layout.html')
@app.route('/FERTILISER', methods=["Get"])
def predict():
    """Fertilizer Suggestions
    Fertilizer Suggestions.
    ---
    parameters:
        - name: Temparature
        in: query
        type: number
        required: true
        - name: Humidity
        in: query
        type: number
        required: true
        - name: Moisture
        in: query
        type: number
        required: true
        - name: Soil_Type
        in: query
        type: text
        required: true
        - name: Crop_Type
        in: query
        type: text
        required: true
        - name: Nitrogen
        in: query
        type: number
        required: true
        - name: Potassium
        in: query
        type: number
        required: true
        - name: Phosphorous
        in: query
        type: number
        required: true

    responses:
        200:
            description: The output values

    """
    Temparature = request.args.get("Temparature")
    Humidity = request.args.get("Humidity")
    Moisture = request.args.get("Moisture")
    Soil_Type = request.args.get("Soil_Type")
    Crop_Type = request.args.get("Crop_Type")
    Nitrogen = request.args.get("Nitrogen")
    Potassium = request.args.get("Potassium")
    Phosphorous = request.args.get("Phosphorous")
    pickle_in = open("fertilizer_model.pkl", "rb")
    classifier = pickle.load(pickle_in)
    prediction = classifier.predict([[Temparature, Humidity, Moisture, Soil_Type,Crop_Type,Nitrogen,Potassium,Phosphorous]])
    
    print(prediction)
    return "we recommend you" + str(prediction)

if __name__ == '__main__':
    app.run(debug=True)
