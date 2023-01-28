from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/page1')
def page1():
    return render_template("page1.html")