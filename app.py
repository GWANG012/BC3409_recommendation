from functions import *
from flask import Flask, make_response
from flask import request, render_template
import pandas as pd
import numpy

app = Flask(__name__)

dataframe = pd.read_csv("Clothing_Inventory_Sample.csv")


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == "POST":
        ladies_men=request.form.get("ladies_men")
        print(type(ladies_men))
        age = request.form.get("age")
        if age!='':
            age = int(age)
        max_price = request.form.get("max_price")
        if max_price!='': 
            max_price = float(max_price)
        colour = request.form.get("colour")
        clothing_style = request.form.get("clothing_style")
        pattern = request.form.get("pattern")
        result = recommendations(dataframe, ladies_men, age, max_price, colour, clothing_style, pattern)
        print(result.info())# result = result.to_html()
        print(type(result))
        resultInfoStr = result.to_html()
        resp = make_response(render_template('index.html', tables = [resultInfoStr]))
        return resp
    else:
        return(render_template('index.html', result="2"))
    
if __name__ == '__main__':
    app.run(debug=True)





