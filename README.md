# Recipe Book | Flask & Mongo DB - Data Centric Development Project

## UX Design

The design was to have an app where there was the freedom to add a recipe you really liked to the Recipe Book App.

## Database Design

The database design was to make it easier for us to maintain by letting the user add their reicpies and this would populate to the Mongo Atlas Database.

## Features

### Existing Features

This is a web application which that allows users to store and easily access recipes. 
It is a full stack web application (frontend and backend) that provides CRUD (Create, Read, Update, Delete) 
functionality to a database hosted in the cloud on Heroku platform as a service. 
Users can :


## Recipes:

•	View details of the Recipes that have already added.
•	You can edit the details of the recipe or delete the recipe.
•	Manage a list of recipes saved by the current logged in user.


## Add Recipe: 

•	Add a new recipe  
•	Add ingredients
•	Add methods

## Demo

A demo of this web application is available [here](https://rpbook.herokuapp.com/).


## Getting started :

1. Clone the repo and cd into the project directory.
2. Ensure you have Python 3 and Postgres installed and create a virtual environment and activate it.
3. Install dependencies: `pip install -r requirements.txt`.


## Technologies Used

**HTML, CSS, JavaScript (Front End Framework Materialize)  Python, Full Stack Micro Framework Flask, Mongo DB an database management system :**

## Testing
Manual testing was undertaken for this application and satisfactorily passed. 
A sample of the tests conducted are as follows:

1.	Testing navigation buttons and hyperlinks throughout the page
2.	Testing the CRUD functionality
3.	Testing the responsiveness of the application on different browsers and then using different devices.

## Deployment
1. Make sure requirements.txt and Procfile exist:
`pip3 freeze --local requirements.txt`
`echo web: python app.py > Procfile`
2. Create Heroku App, Select Postgres add-on, download Heroku CLI toolbelt, login to heroku (Heroku login), 
git init, connect git to heroku (heroku git remote -a <project>), 
git add ., git commit, git push heroku master.
3. heroku ps:scale web=1
4. In heroku app settings set the config vars to add DATABASE_URL, IP and PORT

## Credits

**Matthew Richardson** - This project was completed as part of Code Institute’s Mentored Online Full Stack Web Development course in 2018.

### Content
The content for recipes was taken from the [BBC recipes website](https://www.bbc.com/food/recipes).

### Media
The images for recipes were also taken from the BBC recipes website.
 
