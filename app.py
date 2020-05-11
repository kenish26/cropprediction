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
    crops=['wheat','mungbean','Tea','millet','maize','lentil','jute','cofee','cotton','ground nut','peas','rubber','sugarcane','tobacco','kidney beans','moth beans','coconut','blackgram','adzuki beans','pigeon peas','chick peas','banana','grapes','apple','mango','muskmelon','orange','papaya','watermelon','pomegranate']
    cr='rice'
    
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