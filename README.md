<h1>Recipe Book | Flask & Mongo DB - Data Centric Development Project</H1>

Please click [here](https://rpbook.herokuapp.com/) to visit a live demo of my project.

My Third Milestone Project for Code Institute is a data centric app.
app my idea is to create a The design was to have an app where there was the freedom to add a recipe you really liked to the Recipe Book App.

<H1>UX</H1>

<h2>Who is the target audience?</h2>

A person who is interested in Cooking.
A person who wants to find new recipes.
A person who wantes to add their recipes.

<h2>Why is this the best way to target the audience?</h2>

The app is designed to lead the user to find more recipes.
The app is designed to lead the user to add their own recipes.
The app is designed to lead the user to edit their recipes.
The app is designed to lead the user to view other peoples and make amenend to their recipes if they feel a change is needed.

<h2>User Stories</h2>

<p>•As a user, I want to find more recipes.</P>
<p>•As a user, I want to add my recipes.</p>
<p>•As a user, I want to be able to help people find my recipes</p>
<p>•As a user, I want to be able to help people with amending their recipes after I have tried them</p>

<h2>UX Design</h2>

The UX Designs of the site can be found in the PDF file saved to the project in the file UX Designs.

<h1>Technologies</h1>

<p>•Html</p>
<p>•CSS</P>
<p>•Gitpod - Used for a development and testing area.</P>
<p>•git- Used as a repository.</P></P>
<p>•Heroku - Connected to my Git repositoty to deploy app.</P>
<p>•git- Used as a repository.</P>
<p>•Mongo DB - Database.</P>
<p>•Bootstrap - Bootstrap framework.</P>
<p>•jQuery.</P>

<h1> Features </h1>

The app follows the crud principal, please see below: 

<p>•Create- The user can create a recipe within the site</P>
<p>•Retrive- The user can Retrive a recipe within the site</P> 
<p>•Update- The user can Update a recipe within the site</P> 
<p>•Delete- The user can Delete a recipe within the site</P> 

<h1> Testing </h1>

<p>•I tested the navbar in the chrome browser to ensure that the Home/Recipes/Add Recipe all went to the relevant pages.</P> 
<p>•I tested that the four recipes would display correctly on the front page and that the find out more buttons worked correctly.</P>
<p>•I tested the Recipes page displayed, the recipes that I had added using the form on the add recipe page added the details to the database for the reicpe page to display</P>
<p>•I tested that the CRUD principals are utilised in the app</P>
<p>•I Used W3c validator to validate the html pages created. I copied my code and pasted it into the validator to check for errors and warnings.</P>
<p>•I tested that Heroku had connected properly with my git repository </P>

<h1> Deployment </h1>

1. Make sure requirements.txt and Procfile exist:
`pip3 freeze --local requirements.txt`
`echo web: python app.py > Procfile`
2. Create Heroku App,login to heroku (Heroku login), 
git init, connect git to heroku (heroku git remote -a <project>), 
git add ., git commit, git push heroku master.
3. heroku ps:scale web=1
4. In heroku app settings set the config vars to add DATABASE_URL, IP and PORT

<h2>Media</h2>

The images and recipes were taken from the BBC recipes website.




