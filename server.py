from flask import Flask
from flask import request, redirect, render_template
from API.data_col import price

app = Flask(__name__, template_folder='static')

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)