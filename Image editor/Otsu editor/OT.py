from flask import Flask, render_template, request
import os
import cv2
import numpy as np
from flask import Flask, render_template,url_for
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename



app = Flask(__name__)
UPLOAD_FOLDER = 'C:/Users/sorkg/Documents/OTSUthreshold'
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



my_image = cv2.imread("image.jpg")
image = cv2.cvtColor(my_image, cv2.COLOR_RGB2GRAY)
path = 'C:/Users/sorkg/Documents/OTSUthreshold/static/img'


@app.route('/value')
def value():
    cv2.GaussianBlur(image,(5,5),0)
    ret, outs = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imwrite(os.path.join(path, 'OT.jpg'), outs)
  
   
       
    
    return render_template('value.html')

@app.route('/edit')
def edit():
 

    return render_template("imageprint.html")






if __name__ == '__main__':
    app.run(debug=True)