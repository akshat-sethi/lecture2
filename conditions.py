import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    birth_day = now.month == 6 and now.day == 19
    return render_template("index1.html", birth_day=birth_day) 