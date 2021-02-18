from flask import Flask
from flask import request, redirect, render_template
from API.data_col import price
from login_routes import new_user, verify_user

#app = Flask(__name__, template_folder='static')
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/register")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/user/confirm/<string:decision>", methods = ["POST"])
#string type is either "login" or "signup"
def usercheck(decision):
    print(decision)
    if(decision == "signup"):
        new_user(request.form)
    elif(decision == "login"):
        verify_user(request.form)

    return redirect("/")
@app.route("/<string:random>")
def pageNotFound(random):
    return("404 Error! Page: " + random + " not found ") 

if __name__ == "__main__": 
    app.run(debug=True)