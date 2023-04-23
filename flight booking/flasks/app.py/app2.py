from flask import Flask, render_template,request
import numpy as np
import pickle
import pandas as pd
model = pickle.load(open(r"C:\Users\Gokul Ragavan\Anaconda python\pythonProject1\model1.pk1",'rb'))
app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index3.html')
@app.route("/predict", methods=['POST','GET'])
def predict():
    x = [[int(i) for i in request.form.values()]]
    #print(x)
    # #x=np.array(x)
    #print(x.shape)
    #print(x)
    pred = model.predict(x)
    #print(pred[0])
    return render_template('index3.html', prediction_text=pred[0])
if __name__ == "__main__":
    app.run(debug=False)