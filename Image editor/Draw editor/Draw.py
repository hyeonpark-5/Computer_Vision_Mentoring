from flask import Flask, render_template, request
import os
import cv2
import numpy as np
from flask import Flask, render_template,url_for
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename



app = Flask(__name__)
UPLOAD_FOLDER = 'C:/Users/sorkg/Documents/Draw'
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
image = cv2.imread("image.jpg")
path = 'C:/Users/sorkg/Documents/Draw/static/img'


@app.route('/value', methods= ['POST','GET'])
def value():
    if request.method == 'POST':
        upper = int(request.form['upper'])
        lower = int(request.form['lower'])
        left =  int(request.form['left'])
        right = int(request.form['right'])
        # start_point, end_point = (left, upper),(right, lower)
        # print(start_point)
        # print(end_point)
        image_draw = np.copy(image)
        cv2.rectangle(image_draw, (left,right), (upper,lower), (0, 255, 0),3)
        
        cv2.imwrite(os.path.join(path, 'R.jpg'), image_draw)
        
    return render_template('value.html')


@app.route('/text', methods= ['POST','GET'])
def text():
    if request.method == 'POST':
        textt = str(request.form['textt'])
        textimage=np.copy(image)

        image_draw=cv2.putText(img=textimage,text=textt,org=(10,500),color=(255,255,255),fontFace=4,fontScale=5,thickness=2)
      
        text_image = cv2.cvtColor(image_draw, cv2.COLOR_BGR2RGB)
        cv2.imwrite(os.path.join(path, 'text.jpg'), text_image)
        
   
       
    
    return render_template('text.html')


@app.route('/full', methods= ['POST','GET'])
def full():
    if request.method == 'POST':
        upper = int(request.form['upper'])
        lower = int(request.form['lower'])
        left =  int(request.form['left'])
        right = int(request.form['right'])
        # start_point, end_point = (left, upper),(right, lower)
        # print(start_point)
        # print(end_point)
        full_image = np.copy(image)
        cv2.rectangle(full_image, (left,right), (upper,lower), (0, 255, 0),-1)
        
        cv2.imwrite(os.path.join(path, 'full.jpg'), full_image)
        
    return render_template('full.html')


@app.route('/edit')
def edit():
 

    return render_template("imageprint.html")
    
@app.route('/textimage')
def textimage():
 

    return render_template("imagetext.html")


@app.route('/fullimage')
def fullimage():
 

    return render_template("fullimage.html")






if __name__ == '__main__':
    app.run(debug=True)