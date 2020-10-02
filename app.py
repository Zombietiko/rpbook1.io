from flask import Flask, render_template, redirect, url_for, request
from config import Config
from forms import CreateRecipeForm, EditRecipeForm
from flask_pymongo import PyMongo
import math
import os

app = Flask(__name__)


# app.config['MONGO_URI'] = 'mongodb://localhost:27017/recipeGlut'
app.config['MONGO_URI'] = "mongodb+srv://zombie20:Deco2023!@cluster0.ct2zf.mongodb.net/rp_book?retryWrites=true&w=majority"
app.config['MONGO_URI'] = os.environ.get("MONGODB_URI")
app.config.from_object(Config)

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    """Home page the gets 4 recipes from DB that have been viewed the most"""
    four_recipes = mongo.db.rp_book.find().limit(4)
    return render_template('index.html',recipes=four_recipes)


@app.route('/create_recipe', methods=['GET', 'POST'])
def create_recipe():
    """Creates a recipe and enters into recipe collection"""
    form = CreateRecipeForm(request.form)
    if form.validate_on_submit():
        # set the collection
        recipes_db = mongo.db.rp_book
        # insert the new recipe
        recipes_db.insert_one({
            'title': request.form['title'],
            'short_description': request.form['short_description'],
            'ingredients': request.form['ingredients'],
            'method': request.form['method'],
            'tags': request.form['tags'],
            'image': request.form['image']         
        })
        return redirect(url_for('index', title='New Recipe Added'))
    return render_template('create_recipe.html', title='create a recipe', form=form)


@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """Allows logged in user to edit their own recipes"""
    recipe_db = mongo.db.rp_book.find_one_or_404({'_id': ObjectId(recipe_id)})
    if request.method == 'GET':
        form = EditRecipeForm(data=recipe_db)
        return render_template('edit_recipe.html', recipe=recipe_db, form=form)
    form = EditRecipeForm(request.form)
    if form.validate_on_submit():
        recipes_db = mongo.db.rp_book
        recipes_db.update_one({
            '_id': ObjectId(recipe_id),
        }, {
            '$set': {
                'title': request.form['title'],
                'short_description': request.form['short_description'],
                'ingredients': request.form['ingredients'],
                'method': request.form['method'],
                'tags': request.form['tags'],
                'image': request.form['image'],
            }
        })
        return redirect(url_for('index', title='New Recipe Added'))
    return render_template('edit_recipe.html', recipe=recipe_db, form=form)


@app.route('/delete_recipe/<recipe_id>', methods=['GET', 'POST'])
def delete_recipe(recipe_id):
    """Allows logged in user to delete one of their recipes with added confirmation"""
    recipe_db = mongo.db.rp_book.find_one_or_404({'_id': ObjectId(recipe_id)})
    recipes_db = mongo.db.rp_book
    recipes_db.delete_one({
        '_id': ObjectId(recipe_id)
    })
    return redirect(url_for('index', title='Recipe Glut Updated'))
    

@app.route('/recipes')
def recipes():
    """Logic for recipe list and pagination"""
    # number of recipes per page
    per_page = 8
    page = int(request.args.get('page', 1))
    # count total number of recipes
    total = mongo.db.rp_book.count_documents({})
    # logic for what recipes to return
    all_recipes = mongo.db.rp_book.find().skip((page - 1)*per_page).limit(per_page)
    pages = range(1, int(math.ceil(total / per_page)) + 1)
    return render_template('recipes.html', recipes=all_recipes, page=page, pages=pages, total=total)


@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    """Shows full recipe and increments view"""
    recipe_db = mongo.db.rp_book.find_one_or_404({'_id': ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=recipe_db)


@app.errorhandler(404)
def handle_404(exception):
    return render_template('404.html', exception=exception)


if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = False
    app.config['DEBUG'] = False
    app.run(host='127.0.0.1', debug=False)