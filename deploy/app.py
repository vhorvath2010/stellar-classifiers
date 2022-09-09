import pickle
import flask
import os
from flask import render_template

app = flask.Flask('Stellar Classifier')
PORT = int(os.getenv('PORT', 9099))

rf = pickle.load(open('rf.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    
    features = flask.request.get_json(force=True)['features']
    x = [features['temperature'], features['luminosity'], features['radius'], features['absolute magnitude']]
    prediction = rf.predict([x])
    types = ["Red Dwarf", "Brown Dwarf", "White Dwarf", "Main Sequence", "SuperGiants", "HyperGiants"]
    response = {'prediction': types[prediction[0]]}

    return flask.jsonify(response)

app.run(port=PORT)

@app.route('/')
def home():
    return render_template('index.html')
