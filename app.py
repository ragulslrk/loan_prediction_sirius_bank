from flask import *
import numpy as np
import pandas as pd
import pickle
app = Flask(__name__)  

model = pickle.load(open('loanPrediction.pkl', 'rb'))
#house {2:'rented',0:'norent_noown',1:owned}
# {single:1,married:0}
#car no->0,yes->1

@app.route('/')
def home():
    return ' this is a  home page '


@app.route('/predict/<age>/<experience>/<martial_status>/<house>/<car>',methods=['GET'])
# def predict():
#     age=int(request.form['age'])
#     experience=int(request.form['experience'])
#     martial_status=int(request.form['martial_status'])
#     house=int(request.form['house'])
#     car=int(request.form['car'])
#     values=model.predict(np.array([[age,experience,martial_status,house,car]]))
#     return str(values[0])
def predict(age,experience,martial_status,house,car):
    age=int(age)
    experience=int(experience)
    martial_status=int(martial_status)
    house=int(house)
    car=int(car)
    values=model.predict(np.array([[age,experience,martial_status,house,car]]))
    return str(values[0])

if __name__ =='__main__':  
    app.run()  