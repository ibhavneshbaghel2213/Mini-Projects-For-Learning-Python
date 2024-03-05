

from flask import app, request, render_template, jsonify, Flask
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

scaler = pickle.load(open('Standarization.pkl','rb'))
model = pickle.load(open('boston_regressor.pkl','rb'))

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/predition', methods = ['POST'])
def prediction():
    data = request.json['data']
    new_data = np.array(list(data.values())).reshape(1,-1)
    scaler_data = scaler.transform(new_data)
    result = model.predict(scaler_data)
    return jsonify(result[0])

@app.route('/Predicted', methods = ['POST'])
def predict():
    data = [float(i) for i in request.form.values()]
    scaled_data = scaler.transform(np.array(data).reshape(1,-1))
    result = model.predict(scaled_data)[0]
    return render_template("home.html", predicted_value = "The Predicted Price is {}".format(result))

if __name__ == "__main__":
    app.run(debug=True)