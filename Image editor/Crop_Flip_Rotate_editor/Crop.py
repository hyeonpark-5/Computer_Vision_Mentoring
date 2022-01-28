from flask import Flask, render_template, request
import os
import cv2
import numpy as np
from flask import Flask, render_template,url_for
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename



app = Flask(__name__)
UPLOAD_FOLDER = 'C:/Users/sorkg/Documents/Crop'
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

image = cv2.imread("image.jpg")
path = 'C:/Users/sorkg/Documents/Crop/static/img'


@app.route('/value', methods= ['POST','GET'])
def value():
    if request.method == 'POST':
        upper = int(request.form['upper'])
        lower = int(request.form['lower'])
        left = int(request.form['left'])
        right = int(request.form['right'])
        crop_top = image[upper: lower,:,:]
        crop_horizontal = crop_top[: ,left:right,:]
      
        new_image = cv2.cvtColor(crop_horizontal, cv2.COLOR_BGR2RGB)
        cv2.imwrite(os.path.join(path, 'crop.jpg'), new_image)
        
   
       
    
    return render_template('value.html')

@app.route('/flip')
def flip():
    width, height,C=image.shape
    array_flip = np.zeros((width, height,C),dtype=np.uint8)
    for i,row in enumerate(image):
        array_flip[width-1-i,:,:]=row
        flip_image = cv2.cvtColor(array_flip, cv2.COLOR_BGR2RGB)
        cv2.imwrite(os.path.join(path, 'flip.jpg'), flip_image)


    return render_template("imageprintflip.html")


@app.route('/rotate')
def rotate():              
                                           
    rotate_image1 = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(os.path.join(path, '90rotate.jpg'), rotate_image1)
       
    rotate_image2 = cv2.rotate(image,cv2.ROTATE_180)
    cv2.imwrite(os.path.join(path, '180rotate.jpg'), rotate_image2)
     
    rotate_image3 = cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imwrite(os.path.join(path, '270rotate.jpg'), rotate_image3)

    return render_template('rotate.html')




@app.route('/edit')
def edit():
 

    return render_template("imageprint.html")


@app.route('/rotate1')
def rotate1():
 

    return render_template("rotate90.html")

@app.route('/rotate2')
def rotate2():
 

    return render_template("rotate180.html")

@app.route('/rotate3')
def rotate3():
 

    return render_template("rotate270.html")






if __name__ == '__main__':
    app.run(debug=True)