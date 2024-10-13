from flask import Flask,request, render_template,jsonify
import numpy as np
import pickle
import sklearn

#loading models
pipeline = pickle.load(open('yield_pipeline.pkl','rb'))

#flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/predict",methods=['POST'])
def predict():
    if request.method == 'POST':
        crop = request.form['crop']
        crop_year = request.form['year']
        season = request.form['season']
        state = request.form['state']
        area = request.form['area']
        annual_rainfall  = request.form['rainfall']
        fertilizer  = request.form['fertilizer']
        pesticide  = request.form['pesticide']

        # create an array of the input features
        features = np.array([crop,crop_year,season,state,area,annual_rainfall,fertilizer,pesticide]).reshape(1,-1)

        # Make the prediction
        predicted_yield = pipeline.predict(features)

        # Return the result as JSON
        return jsonify({'prediction': predicted_yield[0]})

        # return render_template('index.html',prediction = predicted_yield[0])

if __name__=="__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)