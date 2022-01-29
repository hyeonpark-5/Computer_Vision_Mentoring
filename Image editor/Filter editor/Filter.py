from flask import Flask, render_template, request
import os
import cv2
import numpy as np
from flask import Flask, render_template,url_for
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename



app = Flask(__name__)
UPLOAD_FOLDER = 'C:/Users/sorkg/Documents/Filter'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def home():
   
    if request.method == 'POST':
        file = request.files['file']
      
        file.save(secure_filename(file.filename))

    return render_template("index.html")



my_image = "image.jpg"
image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
path = 'C:/Users/sorkg/Documents/Filter/static/img'


@app.route('/value', methods= ['POST','GET'])
def value():
    if request.method == 'POST':
        mid = int(request.form['mid'])
        median = cv2.medianBlur(image, mid)
        cv2.imwrite(os.path.join(path, 'median.jpg'), median)
       
    
    return render_template('value.html')

@app.route('/gaussian', methods= ['POST','GET'])
def gaussian():
    if request.method == 'POST':
        d = int(request.form['gaus'])
        gaussian = cv2.GaussianBlur(image,(d,d),0)
        cv2.imwrite(os.path.join(path, 'gaussian.jpg'), gaussian)
       
    
    return render_template('gaussian.html')



@app.route('/edit')
def edit():
 

    return render_template("imageprint.html")

@app.route('/gaussianimage')
def gaussianimage():
 

    return render_template("imagegaussian.html")






if __name__ == '__main__':
    app.run(debug=True)