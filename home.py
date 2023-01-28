from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/your_history')
def your_history():
    return render_template("your_history.html")

@app.route('/add_entry')
def add_entry():
    return render_template("add_entry.html")