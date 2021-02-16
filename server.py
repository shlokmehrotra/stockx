from flask import Flask
from flask import request, redirect, render_template
from data_col import price

app = Flask(__name__, template_folder='static')
stock_name = ""
price_val = ""
@app.route("/")
def index():
    return render_template("testing.html", stock = stock_name, price = price_val)
@app.route('/checkprice', methods = ['POST', 'GET'])
def checkprice():
    stock_name = request.form["stock"]
    print("REQUEST_DATA" + str(stock_name))
    print(price(stock_name))
    price_val = str(price(stock_name))
    return render_template("testing.html", stock = stock_name, price = price_val)
if __name__ == "__main__":
    app.run(debug=True)