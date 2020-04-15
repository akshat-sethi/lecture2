from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Rohan", "Keeyan", "Arkin"]
    return render_template("index2.html", names=names)

@app.route("/more")
def more():
    return render_template("more.html")