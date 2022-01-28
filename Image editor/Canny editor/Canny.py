from flask import Flask, render_template, request
import os
import cv2
import numpy as np
from flask import Flask, render_template,url_for
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename



app = Flask(__name__)
UPLOAD_FOLDER = 'C:/Users/sorkg/Documents/value'
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
path = 'C:/Users/sorkg/Documents/threholding/static/img'


@app.route('/value', methods= ['POST','GET'])
def value():
    if request.method == 'POST':
        thres1 = int(request.form['threshold1'])
        thres2 = int(request.form['threshold2'])
      
        new_image = cv2.Canny(image,thres1, thres2)
        cv2.imwrite(os.path.join(path, 'Canny.jpg'), new_image)
        
   
       
    
    return render_template('value.html')

@app.route('/edit')
def edit():
 

    return render_template("imageprint.html")






if __name__ == '__main__':
    app.run(debug=True)