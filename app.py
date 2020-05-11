# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:36:21 2020

@author: Kenish
"""


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('cp.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    crops=['Black gram', 'Chickpea', 'Coconut', 'Coffee', 'Cotton', 'Ground Nut', 'Jute', 'Kidney Beans', 'Lentil', 'Moth Beans', 'Mung Bean', 'Peas', 'Pigeon Peas', 'Rubber', 'Sugarcane', 'Tea', 'Tobacco', 'apple', 'banana', 'grapes', 'maize', 'mango', 'millet', 'muskmelon', 'orange', 'papaya', 'pomegranate', 'rice', 'watermelon', 'wheat']
    count=0
    for i in range(0,30):
        
        if(prediction[0][i]==1):
            
           c=crops[i]
           count=count+1
           break;
         
        i=i+1
    output =c
    if(count==0):
       print('The predicted crop is %s'%cr)
    else:
       print('The predicted crop is %s'%c)
   

    return render_template('index.html', prediction_text='Predicted crop would be be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
