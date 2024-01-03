from flask import Flask,render_template,request
import pickle
import numpy as np
#for pg render we write render
#@-->used for decoration
application=Flask(__name__)
'''
@app.route("/")
def hello():
    """test fun"""
    return "welcome  flask"
@app.route("/harsha",methods=['GET'])
def check():
    """new func"""
    return "codegnan is in kits guntur"

'''
#First lets read the pickle file
with open('House_Price.pkl','rb')as f:
    model=pickle.load(f)
    
@application.route('/',methods=['GET'])
def home():
    return render_template("index.html")

#api status code
@application.route('/predict',methods=['POST'])
def predict():
    #form action get ayyela cheystadi req in flask
    Rooms=int(request.form['bedrooms'])
    #Rooms -->in pkl script ela undo ala rayali
    #Bedrooms -->html lo ela undo ala rayali
    Bathrooms=int(request.form['bedrooms'])
    Place=int(request.form['location'])
    Area=int(request.form['area'])
    Status=int(request.form['status'])
    Facing=int(request.form['facing'])
    P_Type=int(request.form['type'])
    #now take the above form data and convert to array
    input_data=np.array([[Rooms,Bathrooms,
                          Place,Area,Status,Facing,P_Type]])
    #by taking above data we will predict the house_price
    print(input_data)
    prediction=model.predict(input_data)[0]
    print(prediction)
    #now we will pass above predicted data to template
    return render_template("index.html",
                           prediction=prediction)
application.run()
