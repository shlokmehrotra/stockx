from flask import Flask
from flask import request, redirect, render_template, g, url_for
from flask_mysqldb import MySQL
import yaml

from werkzeug.security import check_password_hash, generate_password_hash

from setup import app, mysql
from API.data_col import price

'''
app = Flask(__name__)

db = yaml.safe_load(open('db.yaml'))

app.config["MYSQL_HOST"] = db["host"]
app.config["MYSQL_USER"] = db["user"]
app.config["MYSQL_PASSWORD"] = db["password"]
app.config["MYSQL_DB"] = db["db_name"]

mysql = MySQL(app)
'''

from login_routes import new_user, verify_user

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register/")
def signup():
    if "auth_mess" not in g:
        g.auth_mess = ""
    return render_template("signup.html", error_message = g.auth_mess)
@app.route("/register/<error>")
def signuperr(error):
    print("hello")
    print(error)
    err = ""
    if(error == "usernameemail"):
        err = "Username and email address are taken"
    elif(error == "email"):
        err = "Email is already taken"
    elif(error == "username"):
        err = "Username is already taken"
    else:
        return redirect("/")
    return render_template("signup.html", error_message = err)
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/showusers")
def display_users():
    cursor = mysql.connection.cursor()
    users = cursor.execute("SELECT * FROM users;")
    if(users > 0):
        values = cursor.fetchall()
        return render_template("userdata.html", userDetails = values)
@app.route("/user/confirm/<string:decision>", methods = ["POST"])
#string type is either "login" or "signup"
def usercheck(decision):
    print(decision)
    if(decision == "signup"):
        rv = new_user(request.form) #outcomes - success, username, email, usernameemail
        return redirect(url_for("signuperr", error = rv))
        #return render_template("signup.html", error_message = err_mess)
        print(rv)
    elif(decision == "login"):
        verify_user(request.form)

    return redirect("/")
@app.route("/<string:random>")
def pageNotFound(random):
    return("404 Error! Page: " + random + " not found ") 

if __name__ == "__main__": 
    app.run(debug=True)