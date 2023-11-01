from flask import Flask,request,render_template,jsonify
import pandas as pd
import numpy as np
import datetime
import os


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('rental.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        pv = request.form.get("pv")
        tenor = request.form.get("tenor")
        r_value=0.22

        pv=float(pv)
        tenor=float(tenor)

        try:
            payment=(pv*(r_value/12))/(1-(1+(r_value/12))** (-tenor))
            rounded_value = round(payment, 2)
        except Exception as e:
            rounded_value="Zero Division Error"
            print("calculateError",e)

        return render_template('rental.html', prediction=rounded_value)

    elif request.method == 'GET':
        return render_template('rental.html')


if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=False)      

