from flask import Flask, render_template
import apsw

app = Flask(__name__)
connection = apsw.Connection("list.db", flags=apsw.SQLITE_OPEN_READWRITE)

# TO DO:
# finalize template design
# login
# populate list

@app.route("/")

def index():
    return render_template("tempdesign.html")