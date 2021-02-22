from flask import Flask
from flask import request, redirect, render_template
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

db = yaml.safe_load(open('./db.yaml'))

app.config["MYSQL_HOST"] = db["host"]
app.config["MYSQL_USER"] = db["user"]
app.config["MYSQL_PASSWORD"] = db["password"]
app.config["MYSQL_DB"] = db["db_name"]

mysql = MySQL(app)

print("successful mysql")
