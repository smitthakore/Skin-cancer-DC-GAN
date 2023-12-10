from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import tensorflow as tf
from PIL import Image
import numpy as np
import os
from keras import models
app = Flask(__name__)
model = models.load_model("C:\\pdpu\\GAN_5\\model\\VGG.h5")
model.compile(loss = 'categorical_crossentropy',
             optimizer = 'adam',
              metrics = ['accuracy'])
UPLOAD_FOLDER = "C:\\pdpu\\GAN_5"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def process_image(image_path):
    img = Image.open(image_path)
    
    img = img.resize((128, 128))  
    img = np.expand_dims(img, axis=0)
    img = np.asarray(img)
    return img



@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        if 'img' not in request.files:
            return redirect(request.url)

        file = request.files['img']
        
        if file.filename == '':
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            processed_image = process_image(file_path)
        
            prediction = model.predict(processed_image)
            prediction = np.argmax(prediction,axis=1)
            result = "Result: " + str(prediction)

            return render_template('result.html', result=result)

    return render_template('home.html')

@app.route('/tryme', methods=['GET', 'POST'])

def home2():
    return render_template('h2.html')


if __name__ == '__main__':
    app.run(debug=True)