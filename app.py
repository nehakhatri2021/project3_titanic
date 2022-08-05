
import numpy as np
from flask import Flask, request, jsonify, render_template

import pickle


app = Flask(__name__)
model = pickle.load(open('knn_model.pkl','rb')) 


@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    
    
    '''
    For rendering results on HTML GUI
    '''
    #result=np.array(['SqFt','bedrooms','Offers','bricks','Neighborhood','Bathrooms'])
    #result.reshape(1,-1)
    #print(result)
    r1 = float(request.args.get('Age'))
    r2 = float(request.args.get('SibSp'))
    r3 = float(request.args.get('Parch'))
    r4 = float(request.args.get('Fare'))
    r5 = float(request.args.get('Gender'))
    r6 = float(request.args.get('Pclass'))
    result=np.array([r1,r2,r3,r4,r5,r6]).reshape(1,-1)
    prediction = model.predict(result)
    
    if  prediction==0:
      return render_template('index.html', prediction_text='Unfortunately, the person will not survive')
    else:
      return render_template('index.html', prediction_text='Luckily, the person will survive')
 


if __name__ == '__main__':
    app.run(debug=True)
