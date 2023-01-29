from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb+srv://sophellwood:PfltNb2uap44RwfG@cluster0.5uhkvsi.mongodb.net/mydb?retryWrites=true&w=majority"

mongo = PyMongo(app)

names = mongo.db.qhacks


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/your_history')
def your_history():
    saved_entries = names.find()
    return render_template("your_history.html", entries = saved_entries)

@app.route('/add_entry')
def add_entry():    
    return render_template("add_entry.html")

@app.route('/add_todo', methods=['POST'])
def add_todo():
    new_date = request.form.get('add-date')
    new_time = request.form.get('add-time')
    new_symptom = request.form.get('add-symptom')
    new_rating = request.form.get('add-rating')
    names.insert_one({'date' : new_date, 'time' : new_time, 'symptom' : new_symptom, 'rating' : new_rating,'complete' : False})
    return redirect(url_for('your_history'))

@app.route('/suggestions')
def suggestions():    
    return render_template("suggestions.html")