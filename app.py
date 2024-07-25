from flask import Flask, render_template
import apsw

app = Flask(__name__)
connection = apsw.Connection("list.db", flags=apsw.SQLITE_OPEN_READWRITE)

# TO DO:
# finalize template design
# change list to table
# login
# populate list
# add links to each film -> where to watch popup; mark as watched

@app.route("/")

def index():
    return render_template("tempdesign.html")