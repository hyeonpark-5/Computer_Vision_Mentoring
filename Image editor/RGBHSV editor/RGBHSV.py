from flask import Flask, render_template, request
import os
import cv2
import numpy as np
from flask import Flask, render_template,url_for
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename



app = Flask(__name__)
UPLOAD_FOLDER = 'C:/Users/sorkg/Documents/RGBHSV'
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
image = cv2.imread(my_image)
path = 'C:/Users/sorkg/Documents/RGBHSV/static/img'


@app.route('/value', methods= ['POST','GET'])
def value():
    
    return render_template('value.html')




@app.route('/RED')
def RED():
     image_Red = image.copy()
     image_Red[:, :, 1] = 0
     image_Red[:, :, 2] = 0
     plt.figure(figsize=(10, 10))
     Red = cv2.cvtColor(image_Red, cv2.COLOR_BGR2RGB)

     cv2.imwrite(os.path.join(path, 'red.jpg'), Red)
    
     return render_template("imageprint.html")


@app.route('/BLUE')
def BLUE():
    image_blue = image.copy()
    image_blue[:, :, 0] = 0
    image_blue[:, :, 1] = 0
    plt.figure(figsize=(10, 10))
    Blue = cv2.cvtColor(image_blue, cv2.COLOR_BGR2RGB)
  
    cv2.imwrite(os.path.join(path, 'blue.jpg'), Blue)
   
 
    return render_template("BLUE.html")

@app.route('/GREEN')
def GREEN():
    image_green = image.copy()
    image_green[:, :, 0] = 0
    image_green[:, :, 2] = 0
    plt.figure(figsize=(10,10))

    Green = cv2.cvtColor(image_green, cv2.COLOR_BGR2RGB)
    cv2.imwrite(os.path.join(path, 'green.jpg'), Green)
   
 
    return render_template("GREEN.html")

hsv_image = cv2.imread("image.jpg", cv2.IMREAD_COLOR)
hsv= cv2.cvtColor(hsv_image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

@app.route('/HSV', methods= ['POST','GET'])
def HSV():
    
    return render_template('hsv.html')

@app.route('/Hue')
def Hue():
 
    cv2.imwrite(os.path.join(path, 'hue.jpg'), h)
   
 
    return render_template("Hue.html")

@app.route('/Saturation')
def Saturation():
 
    cv2.imwrite(os.path.join(path, 'saturation.jpg'), s)
   
 
    return render_template("Saturation.html")


@app.route('/V')
def V():
 
    cv2.imwrite(os.path.join(path, 'value.jpg'), v)
   
 
    return render_template("V.html")

if __name__ == '__main__':
    app.run(debug=True)