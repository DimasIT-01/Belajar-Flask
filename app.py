import numpy as np
from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential, load_model
from keras.models import load_model
application = Flask(__name__)

def get_model():
    global model
    model=load_model("simple_model.h5")
    
 
@application.route('/')
def index():
    return render_template('index.html')

@application.route('/predict',methods=['POST'])
def predict():
    model=load_model("simple_model.h5")
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    return render_template('index.html', prediction_text='kemungkinan tinggi sungai {}'.format(prediction))
    
if __name__ == '__main__':
    application.run(debug=True)