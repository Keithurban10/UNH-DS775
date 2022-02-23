from winreg import HKEY_LOCAL_MACHINE
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def Home():
    personName = "Kealian"
    petList = ('cats','dogs','fish')
    return render_template("base.html", person=personName, list=petList)

@app.route("/admin")
def admin():
    return render_template("base.html")