from flask import Flask, render_template, request 
from werkzeug.utils import secure_filename
import os
from keras.models import load_model
import cv2
import numpy as np

app = Flask(__name__)

model = load_model('weights.best.inc.attractive.hdf5')

UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def attractive_prediction(file):
  if file is None or not allowed_file(file.filename):
    print("Invalid or missing image file.")
    return 0

  filename = secure_filename(file.filename)
  filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
  file.save(filepath)

  im = cv2.imread(filepath)
  if im is None:
    print(f"Error loading image: {filepath}")
    return 0

  im = cv2.resize(cv2.cvtColor(im, cv2.COLOR_BGR2RGB), (178, 218)).astype(np.float32) / 255.0
  im = np.expand_dims(im, axis=0)

  result = model.predict(im)
  print(f'\n\nResult: {result[0]}\n\n')
  return result[0][1]

@app.route('/', methods=['GET', 'POST'])
def home():
  return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def prediction():
  name = request.form.get('name')
  result = f'{name}, Your uploaded image is not attractive.'

  if 'img' in request.files:
    file = request.files['img']
    pred = attractive_prediction(file)
    if pred > 0.5:
      result = f'{name}, Your uploaded image is attractive.'
  
  return render_template('prediction.html', prediction=result, percentage=round(pred * 100, 3))

if __name__ == '__main__':
  app.run(debug=True)
