from flask import Flask, render_template, request
import os
import cv2
import numpy as np
from flask import Flask, render_template,url_for
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename

grayimage = cv2.imread("image.jpg",cv2.IMREAD_GRAYSCALE) #brightness

#file save (파일 저장)
app = Flask(__name__)
UPLOAD_FOLDER = 'C:/Users/sorkg/Documents/Main_Application'
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
my_image2 = cv2.imread("image.jpg") #RGB, HSV
image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE) #Canny/median/gaussian
image2 = cv2.imread("image.jpg") #Crop/Flip/Rotate/Rectangle/FullRectangle/text
image3 = cv2.cvtColor(my_image2, cv2.COLOR_RGB2GRAY) #Otsu
path = 'C:/Users/sorkg/Documents/Main_Application/static/img'

#Canny editor
@app.route('/value', methods= ['POST','GET'])
def value():
    if request.method == 'POST':
        thres1 = int(request.form['threshold1'])
        thres2 = int(request.form['threshold2'])
      
        new_image = cv2.Canny(image,thres1, thres2)
        cv2.imwrite(os.path.join(path, 'canny.jpg'), new_image)
        
   
       
    
    return render_template('value.html')


#Crop editor
@app.route('/crop', methods= ['POST','GET'])
def crop():
    if request.method == 'POST':
        upper = int(request.form['upper'])
        lower = int(request.form['lower'])
        left = int(request.form['left'])
        right = int(request.form['right'])
        crop_top = image2[upper: lower,:,:]
        crop_horizontal = crop_top[: ,left:right,:]
      
        new_image = cv2.cvtColor(crop_horizontal, cv2.COLOR_BGR2RGB)
        cv2.imwrite(os.path.join(path, 'crop.jpg'), new_image)
        
    
    return render_template('crop.html')


#Flip editor, Flip image
@app.route('/flip')
def flip():
    width, height,C=image2.shape
    array_flip = np.zeros((width, height,C),dtype=np.uint8)
    for i,row in enumerate(image2):
        array_flip[width-1-i,:,:]=row
        flip_image = cv2.cvtColor(array_flip, cv2.COLOR_BGR2RGB)
        cv2.imwrite(os.path.join(path, 'flip.jpg'), flip_image)


    return render_template("flipimage.html")


#Rotate editor
@app.route('/rotate')
def rotate():              
                                           
    rotate_image1 = cv2.rotate(image2,cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(os.path.join(path, '90rotate.jpg'), rotate_image1)
       
    rotate_image2 = cv2.rotate(image2,cv2.ROTATE_180)
    cv2.imwrite(os.path.join(path, '180rotate.jpg'), rotate_image2)
     
    rotate_image3 = cv2.rotate(image2,cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imwrite(os.path.join(path, '270rotate.jpg'), rotate_image3)

    return render_template('rotate.html')

#Draw Rectangle image
@app.route('/rec', methods= ['POST','GET'])
def rec():
    if request.method == 'POST':
        upper = int(request.form['upper'])
        lower = int(request.form['lower'])
        left =  int(request.form['left'])
        right = int(request.form['right'])
        # start_point, end_point = (left, upper),(right, lower)
        # print(start_point)
        # print(end_point)
        image_draw = np.copy(image2)
        cv2.rectangle(image_draw, (left,right), (upper,lower), (0, 255, 0),3)
        
        cv2.imwrite(os.path.join(path, 'R.jpg'), image_draw)
        
    return render_template('rec.html')

#Draw Rectangle filled with color
@app.route('/fullrec', methods= ['POST','GET'])
def fullrec():
    if request.method == 'POST':
        upper = int(request.form['upper'])
        lower = int(request.form['lower'])
        left =  int(request.form['left'])
        right = int(request.form['right'])
        # start_point, end_point = (left, upper),(right, lower)
        # print(start_point)
        # print(end_point)
        full_image = np.copy(image2)
        cv2.rectangle(full_image, (left,right), (upper,lower), (0, 255, 0),-1)
        
        cv2.imwrite(os.path.join(path, 'full.jpg'), full_image)
        
    return render_template('fullrec.html')

#Draw text editor
@app.route('/text', methods= ['POST','GET'])
def text():
    if request.method == 'POST':
        textt = str(request.form['textt'])
        textimage=np.copy(image2)

        image_draw=cv2.putText(img=textimage,text=textt,org=(10,500),color=(255,255,255),fontFace=4,fontScale=5,thickness=2)
      
        text_image = cv2.cvtColor(image_draw, cv2.COLOR_BGR2RGB)
        cv2.imwrite(os.path.join(path, 'text.jpg'), text_image)
        
   
       
    
    return render_template('text.html')

#median filter editor
@app.route('/median', methods= ['POST','GET'])
def median():
    if request.method == 'POST':
        mid = int(request.form['mid'])
        median = cv2.medianBlur(image, mid)
        cv2.imwrite(os.path.join(path, 'median.jpg'), median)
       
    
    return render_template('median.html')


#Gaussian filter editor
@app.route('/gaussian', methods= ['POST','GET'])
def gaussian():
    if request.method == 'POST':
        d = int(request.form['gaus'])
        gaussian = cv2.GaussianBlur(image,(d,d),0)
        cv2.imwrite(os.path.join(path, 'gaussian.jpg'), gaussian)
       
    
    return render_template('gaussian.html')


#Otsu editor
@app.route('/otsu')
def otsu():
    cv2.GaussianBlur(image3,(5,5),0)
    ret, outs = cv2.threshold(image3, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imwrite(os.path.join(path, 'OT.jpg'), outs)
  
    
    return render_template('otsu.html')


#RGB editor
@app.route('/rgb', methods= ['POST','GET'])
def rgb():
    
    return render_template('rgb.html')


#HSV editor
@app.route('/hsv', methods= ['POST','GET'])
def hsv():
    
    return render_template('hsv.html')


#Brightness editor
@app.route('/brightness', methods= ['POST','GET'])
def brightness():
    if request.method == 'POST':
        V = int(request.form['bright'])
        print(V)
        alpha = 1 
        beta = V  #brightness control   
        new_image = cv2.convertScaleAbs(grayimage, alpha=alpha, beta=beta)
        cv2.imwrite(os.path.join(path, 'brightness.jpg'), new_image)
        
   
        
    
    return render_template('brightness.html')

#Canny image
@app.route('/cannyimage')
def cannyimage():
 

    return render_template("imageprint.html")

#Crop image
@app.route('/cropimage')                                
def cropimage():
 

    return render_template("cropimage.html")

#Rotate 90 image
@app.route('/rotate1')
def rotate1():
 

    return render_template("rotate90image.html")


#Rotate 180 image
@app.route('/rotate2')
def rotate2():
 

    return render_template("rotate180image.html")

#Rotate 270 image
@app.route('/rotate3')
def rotate3():
 

    return render_template("rotate270image.html")

#Rectangle image
@app.route('/recimage')
def recimage():
 

    return render_template("recimage.html")

#Rectangle filled with color image
@app.route('/fullrecimage')
def fullrecimage():
 

    return render_template("fullrecimage.html")

#text image
@app.route('/textimage')
def textimage():
 

    return render_template("textimage.html")

#median image
@app.route('/medianimage')
def medianimage():
 

    return render_template("medianimage.html")


#gaussian image
@app.route('/gaussianimage')
def gaussianimage():
 

    return render_template("gaussianimage.html")


#Otsu image
@app.route('/otsuimage')
def otsuimage():
 

    return render_template("otsuimage.html")

#Red image
@app.route('/redimage')
def redimage():
     image_Red = my_image2.copy()
     image_Red[:, :, 1] = 0
     image_Red[:, :, 2] = 0
     plt.figure(figsize=(10, 10))
     Red = cv2.cvtColor(image_Red, cv2.COLOR_BGR2RGB)

     cv2.imwrite(os.path.join(path, 'red.jpg'), Red)
    
     return render_template("redimage.html")


#Blue image
@app.route('/blueimage')
def blueimage():
    image_blue = my_image2.copy()
    image_blue[:, :, 0] = 0
    image_blue[:, :, 1] = 0
    plt.figure(figsize=(10, 10))
    Blue = cv2.cvtColor(image_blue, cv2.COLOR_BGR2RGB)
  
    cv2.imwrite(os.path.join(path, 'blue.jpg'), Blue)
   
 
    return render_template("blueimage.html")

#Green image
@app.route('/greenimage')
def greenimage():
    image_green = my_image2.copy()
    image_green[:, :, 0] = 0
    image_green[:, :, 2] = 0
    plt.figure(figsize=(10,10))

    Green = cv2.cvtColor(image_green, cv2.COLOR_BGR2RGB)
    cv2.imwrite(os.path.join(path, 'green.jpg'), Green)


    return render_template("greenimage.html")

#hsv 
hsv_image = cv2.imread("image.jpg", cv2.IMREAD_COLOR)
hsv= cv2.cvtColor(hsv_image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

#Hue iamge
@app.route('/Hue')
def Hue():
 
    cv2.imwrite(os.path.join(path, 'hue.jpg'), h)
   
 
    return render_template("Hueimage.html")


#Saturation image
@app.route('/Saturation')
def Saturation():
 
    cv2.imwrite(os.path.join(path, 'saturation.jpg'), s)
   
 
    return render_template("Saturationimage.html")


#value image
@app.route('/V')
def V():
 
    cv2.imwrite(os.path.join(path, 'value.jpg'), v)
   
 
    return render_template("Vimage.html")


#Brightness image
@app.route('/brightnessimage')
def brightnessimage():
 

    return render_template("brightnessimage.html")


if __name__ == '__main__':
    app.run(debug=True)