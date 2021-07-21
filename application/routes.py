from application import app
from flask import render_template, request, json, jsonify
import requests
import os
# import numpy
# import pandas as pd

# decorator to access the app
@app.route("/")
@app.route("/index")
def index():
    bank_image = os.path.join(app.config['UPLOAD_IMAGE'], 'bank_loan.png')
    return render_template("index.html", bank_image=bank_image)

# decorator to access the service
@app.route("/bankclassify", methods=['GET', 'POST'])
def bankclassify():
    bank_image = os.path.join(app.config['UPLOAD_IMAGE'], 'bank_loan.png')
    # extract form inputs
    age = request.form.get("age")
    job = request.form.get("job")
    marital = request.form.get("marital")
    education = request.form.get("education")
    default = request.form.get("default")
    balance = request.form.get("balance")
    housing = request.form.get("housing")
    loan = request.form.get("loan")

    # convert data to json
    input_data = json.dumps({"age": age, "job": job, "marital": marital, "education": education, "default": default, "balance": balance, "housing": housing, "loan": loan})

    # url for bank marketing model
    # Test
    url = "http://localhost:3000/api"
    # Stage
    # url = "https://bank-model-app.herokuapp.com/api"
  
    # post data to url
    conn_exception = ''
    results = ''
    try:
        result = requests.post(url, input_data)
        # decode to UTF-8
        results = result.content.decode('UTF-8')

    except requests.exceptions.Timeout:
        conn_exception = 'Timeout, retry later'
        pass

    except requests.exceptions.RequestException as e:
        conn_exception = 'Prediction service not available'
        pass

    # send input values and prediction result to index.html for display
    return render_template("index.html", bank_image=bank_image, conn_exception=conn_exception,
                           age=age, job=job, marital=marital, education=education,
                           default=default, balance=balance, housing=housing,
                           loan=loan,  results=results)
