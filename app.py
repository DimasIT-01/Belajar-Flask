import numpy as np
from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential, load_model
from keras.models import load_model
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/predict',methods=['POST'])
def predict():
    model=tf.saved_model.load('saved_model')
     hujan=request.form.get("rainfall", type=float)
    sinar=request.form.get("sunshine_duration", type=float)
    suhu=request.form.get("temperature_avg", type=float)
    angin=request.form.get("wind_speed_avg", type=float)
    lembap=request.form.get("humidity_avg", type=float)
    input= [ [hujan ,sinar ,suhu, angin, lembap] ]
    prediction = model(input)
    return render_template('index.html', prediction_text='kemungkinan tinggi sungai {}'.format(prediction))
    
if __name__ == '__main__':
    application.run(debug=True)
