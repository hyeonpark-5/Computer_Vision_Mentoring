from flask import Flask, render_template, request
import os
import cv2
import numpy as np
from flask import Flask, render_template,url_for
import matplotlib.pyplot as plt
my_image = "image.jpg"
path = 'C:/Users/sorkg/Documents/value/static/img'
goldhill = cv2.imread("image.jpg",cv2.IMREAD_GRAYSCALE)
app = Flask(__name__)

@app.route('/', methods= ['POST','GET'])
def home():
    if request.method == 'POST':
        V = int(request.form['u'])
        print(V)
        alpha = 1 # Simple contrast control
        beta = V  # Simple brightness control   
        new_image = cv2.convertScaleAbs(goldhill, alpha=alpha, beta=beta)
        cv2.imwrite(os.path.join(path, 'brightness.jpg'), new_image) #static/image에 brightness.jpg이름으로 저장
       
    
    return render_template('value.html')

@app.route('/edit')
def edit():
 

    return render_template("imageprint.html")






if __name__ == '__main__':
    app.run(debug=True)