from flask import Flask, render_template, redirect, url_for, request
from config import Config
from forms import CreateRecipeForm, EditRecipeForm
from flask_pymongo import PyMongo
import math
import os

app = Flask(__name__)


# app.config['MONGO_URI'] = 'mongodb://localhost:27017/recipeGlut'
#app.config['MONGO_URI'] = "mongodb+srv://zombie20:Deco2023!@cluster0.ct2zf.mongodb.net/rp_book?retryWrites=true&w=majority"
app.config['MONGO_URI'] = os.environ.get("MONGODB_URI")
app.config.from_object(Config)

mongo = PyMongo(app)


@app.route('/')
@app.route('/test.html')
def index():
    """Home page the gets 4 recipes from DB that have been viewed the most"""
   # four_recipes = mongo.db.rp_book.find().limit(4)
   # return render_template('index.html',recipes=four_recipes)

    four_recipes = 'hello!!'
    return render_template('test.html',four_recipes=four_recipes)



@app.errorhandler(404)
def handle_404(exception):
    return render_template('404.html', exception=exception)


if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = False
    app.config['DEBUG'] = False
    app.run(host='127.0.0.1', debug=False)