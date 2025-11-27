from flask import Flask,render_template, request,jsonify
from flask_cors import CORS
import pandas as pd
import joblib
import os

#Create BackEnd App using Flask
app = Flask(__name__)

#Giving CORS permission to my app
CORS(app)

#Load the Model PKL file
pipeline = joblib.load("model.pkl")  


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/load-data")
def LoadData():
    encoder = pipeline.named_steps['preproc'].named_transformers_['cat'].named_steps['onehot'].categories_
    print(encoder[1])
    return jsonify({"BrandData":encoder[1].tolist()})


@app.route("/predict",methods=["POST"])
def predict():
    data = request.json
    input_data = pd.DataFrame({
    "kms_driven": [int(data['kms_driven'])],
    "owner": [data['owner']],
    "power": [int(data['power'])],
    "brand": [data['brand']],
    "Original Price": [int(data['Original Price'])],
    "year": [int(data['year'])]})
    
    result =  pipeline.predict(input_data);
    
    return jsonify({"predictedPrice": f"{result[0]:,.2f}"})

if __name__ == '__main__':
    port = int (os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port, debug=True)