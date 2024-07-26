from flask import Flask, render_template
import apsw
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
connection = apsw.Connection("list.db", flags=apsw.SQLITE_OPEN_READWRITE)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# TO DO:
# finalize template design
# change list to table
# login
# populate list
# add links to each film -> where to watch popup; mark as watched

@app.route("/")
def index():
    return render_template("tempdesign.html")

@app.route("/login")
def login():
    return "to do"