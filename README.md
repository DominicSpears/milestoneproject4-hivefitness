# Hive Fitness - An online fitness community!

Welcome to Hive Fitness, a website for users all over the world buy top quality 
fitness equipment in order to reach their training goals. It also includes a blog
wgich is regularly updated with arlicles about a variety of fitness topics.  This 
allows our customers to comment and discuss these topics with a community of like 
minded people. Made for my Code Institute Milestone Project 4.

Follow the link to [Hive Fitness](#deployed app url)

![Responsive Example](#)

### Contents

* [Introduction](#intro) 

* [UX](#ux)
  * [Strategy Plane](#strategy)
  * [Scope Plane](#scope)
  * [Structure Plane](#structure)
  * [Skeleton Plane](#skeleton)
  * [Surface Plane](#surface)

* [Technologies](#tech) 
  * [Languages](#languages)
  * [Database](#database)
  * [Libraries](#libraries)
  * [Tools](#tools)
  * [Hosting](#hosting)

* [Features](#feat)
  * [Current logins](#current)
  * [Active features](#active)
  * [Future features](#future)

* [Testing](#test)

* [Deployment](#deploy)
  * [Deploy project](#deploy)
  * [Run project](#run)
  * [Clone project](#clone)

* [Credits](#credit)
  * [Code credits](#code)
  * [Media credits](#media)
  * [Acknowledgements](#acknowledgements)
___

<a name="intro"></a>

### Introduction

This website is designed to be a full stack development project. By doing so users have 
access to a fully functioning e-store and can order a wide variety of fitness equipment. 
Each product has it's own page with information, cost and rating. Also visitors have access 
to a blog which covers a wide range of topics from latest product reviews to training tips 
and ideas. By signing up as a user, visitors can leave comments on specific stricles and 
posts, enabling them to become part of the discussion. 
___

<a name="ux"></a>

### UX

<a name="strategy"></a>

### Strategy Plane
#### Potential Users

Target Audience
* People who are fitness enthusiasts
* People who are interested in trying a new workout plan
* People who want to replace a peice of equipment
* People who wish to join an online fitness community

Visitor / User Goals
* Purchase products in a smooth and secure way
* Get informed with the products before buying by product ratings / product information
* Gain knowledgefrom blog articles and leave comments on those blog articles

Business Goals (Site Owner's Goals)
* Provide customers with a secure and safe online store
* Establish the shop's brand image
* Expand the business with a community blog
* Make profit from selling products

<a name="scope"></a>

### Scope Plane
#### Features specific for users

Casual Visitor
* Welcoming homepage
* A way to register and become a user
* Easy to use navigation bar
* Information about the site
* A way to contact the site administrators
* Access to the blog articles

Shopper
* Easy access to the shop from all pages of the site
* Clear product layout with images
* Easy to absorb product information
* Product categories to narrow the search
* A product search bar
* A way to order selected products by price/categoy/etc
* A simple shopping bag

Registered user
* A personal profile page
* Secure login
* Saved personal information
* Links to additional social media
* Leave comments on the blog

Site administrator
* Add, edit or delete products as required
* Allow management of product categories
* Add, edit or delete post articles as required
* Allow management of post categories
* Number of comments on a specific article
* Edit or delete any blog comment

<a name="structure"></a>

### Structure Plane
#### User stories

|As a/an           |I want to be able to                         |So that I can                                           |
|------------------|---------------------------------------------|--------------------------------------------------------|
|Casual Visitor    |Read information about the site              |Know what the site offers                               |
|Casual Visitor    |Easily navigate the site                     |Access any specific tool or product                     |
|Casual Visitor    |Regiter with the site                        |Become a user                                           |
|Casual Visitor    |See all blog articles                        |Access the information provided                         |
|Casual Visitor    |Contact the site administrators              |Report a problem/ request information                   |
|------------------|---------------------------------------------|--------------------------------------------------------|
|Shopper           |Access the shop from any page of the site    |Get to the shop easily                                  |
|Shopper           |See a display of all products                |Scan through the site's full collection                 |
|Shopper           |Click on a product                           |See extra information an a rating                       |
|Shopper           |Search for products                          |Look for specific items                                 |
|Shopper           |Narrow down the products by category         |See all items in a specfic genre                        |
|Shopper           |Order the products by price/category/etc     |Easily search through a long list of items              |
|Shopper           |Review my order in a checkout                |Check that my order is correct before confirmation      |
|------------------|---------------------------------------------|--------------------------------------------------------|
|Registered User   |Save personal information                    |Enter it once only                                      |
|Registered User   |See a profile page                           |Add or update my personal information                   |
|Registered User   |See a list of previous orders                |Confirm what I have already purchased and when          |
|Registered User   |Register my own login information            |Log into the site securely                              |
|Registered User   |Get to associated social media sites         |Get further information/content                         |
|Registered User   |Leave comments on any blog post              |Be part of the community discussion                     |
|------------------|---------------------------------------------|--------------------------------------------------------|
|Site administrator|Add, edit or delete products as required     |Maintain the online shop                                |
|Site administrator|Manage the product categories                |Ensure the products can be easily searched/narrowed down|
|Site administrator|Add, edit or delete post articles as required|Maintain the blog posts                                 |
|Site administrator|Manage the post categories                   |Ensure the posts can be easily searched/narrowed down   |
|Site administrator|See the number of comments on each post      |Indicate which posts are getting the most traffic       |
|Site administrator|Edit or delete a blog comment                |Update mistakes or remove inappropriate content         |

<a name="skeleton"></a>

### Skeleton Plane
#### Wireframes

[Mobile Wireframes](#)

[Tablet Wireframes](#)

[Desktop Wireframes](#)

<a name="surface"></a>

### Surface Plane

* Background - Yellow
* Navbar - Grey/black
* Colours/font colours – Black / grey, yellow.  
___

<a name="tech"></a>

### Technologies

Technologies used to create the site:

<a name="languages"></a>

#### Languages
* HTML 
  * The project uses **HTML 5** to create the basic layout and site structure.
* CSS
  * The project uses **CSS 3** to style the html to be aesthetically pleasing and responsive.
* JavaScript
  * The project uses **JavaScript** to provide an interactive experience and functionality.. 
* Python
  * The project uses **Python3** to link the main site and the database. 
* Django
  * The project uses **Django3** as a framework for python. 

<a name="database"></a>

#### Database
* [Mongo DB](https://www.mongodb.com/)
  * the project uses **mongo db** as a database provider to store various forms of information.
  * ![Database Schema](#)

<a name="libraries"></a>

#### Libraries
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
  * the project uses **flask** as an application framework to aid the creation of complex applications.
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
  * the project uses **jinja v3.0.1** as a templating engine to allow writing code similar to python syntax.
* [PyMongo](https://pypi.org/project/pymongo/)
  * the project uses **pymongo v3.11.4** to connect python code to the mongo database.
* [Materialize](https://flask.palletsprojects.com/en/2.0.x/)
  * the project uses **materialize** as a responsive front-end framework based on material design.
* [Font Awesome](https://fontawesome.com/) 
  * The project uses **Font Awesome Version 5.15.1** to add icons that aid aesthetics or provide social media links.
* [Google Fonts](https://fonts.google.com/)
  * the project uses **google fonts** as a source for its extra fonts.

<a name="tools"></a>

#### Tools
* [Git](https://git-scm.com/)
  * The project uses **git** as version control.
* [Github](https://github.com/)
  * The project uses **Github** to provide hosting for the development process.
* [Gitpod](https://www.gitpod.io/)
  * The project uses **Gitpod** as a development environment in the browser.
* [Color Dropper](https://chrome.google.com/webstore/detail/color-dropper/cbagleaaaocejmdeichhdkmjebpljckh)
  * The project uses the **color dropper** (a Chrome add on) to help select colors.
* [Balsamiq](https://flask.palletsprojects.com/en/2.0.x/)
  * the project uses **balsamiq** as a wireframing tool to plan the layout of the site.
* [Am I responsive]()
  * the project uses **am i responsive** to create the readme hero image.

<a name="hosting"></a>

#### Hosting 
* [Heroku](https://www.heroku.com/home)
  * the project uses **heroku** as to deploy, manage, and scale the site.
___

<a name="feat"></a>

### Features

<a name="current"></a>

#### Current logins
I have created an administrator and a selection and users for you to test the features
available to the differernt roles. 

|Username       |Password       |Role           |
|---------------|---------------|---------------|
|admin          |manage12345    |Administrator  |
|domSpears      |user12345      |User           |
|annexample     |example12345   |User           |
|johnsmith      |example12345   |User           |

<a name="active"></a>

#### Register Page
* Username and password input
* Register button, adds new user details to the database
* Link to login page

#### Login Page
* Username and password input
* Login button, logs existing user into the site, to their profile page
* Link to register page

#### Navbar
* Brand logo links to homepage
* Navbar buttons link to individual pages
* Certain nav links only appear when a user or an admin is logged in
* Log out button ends session

#### Footer
* Links to social media sites, bring up a new tab

#### Home Page
* Link to cookware and recipe page
* If a user/admin is logged in, link to profile page
* If no user/admin is logged in, link to login page

#### Cookware Page
* Add cookware button links to add cookware page (admin only)
* For loop reveals all cookware items in the database
* Website button linked to online store for idividual item
* Edit button links to edit cookware page (admin only)
* Delete button removes item from database (admin only)
* Delete modal to confirm removal of an item

#### Add Cookware Page
* Inputs for item name, price, image and website link
* Confirmation button add item to the database
* Cancel button returns user to cookware page
* Add modal to confirm addition of an item

#### Edit Cookware Page
* Input fields show existing data
* Confirmation button linked to confirmation modal
* Cancel button returns user to cookware page
* Edit modal to confirm update of an item

#### Recipe Page
* For loop reveals all recipes in the database
* Search reveals recipes based on the recipe name or cuisines
* Reset button returns all recipes to the page
* Full recipe button linked to view recipe page

#### View Recipe Page
* Displays all recipe information from the database
* Dietary requirements (vegetarian, vegan, spicy) displayed with 
color coded icons, grey for no, colored for yes

#### Add Recipe Page (User only)
* Input fields for all recipe information
* Cuisine dropdown gets options from the database
* Dietary requirement switches
* Ingredients/method input will recieve a custom number of items
* Plus button adds an input, minus removes an input
* Confirmation button adds a recipe to the database
* Cancel button returns user to recipe page

#### Profile Page
* For loop shows all recipes matching the username(user)
* For loop shows all recipes(admin)
* Full recipe button linked to view recipe page
* Edit button linked to edit recipe page
* Delete button linked to confirmation modal
* Delete modal removes recipe from database

#### Edit Recipe Page
* Input fields show existing data
* Confirmation button linked to confirmation modal 
* Cancel button returns user to profile page
* Edit modal updates recipe in the database

#### User Page (admin only)
* For loop shows all user in the database
* Edit button linked to edit user page
* Delete buttom linked to confirmation modal
* Delete modal removed user from database

#### Edit user Page
* Input fields show existing data
* Switch allows users to be made administrators
* Confirmation button linked to confirmation modal
* Cancel button returns user to cookware page
* Edit modal to confirm update of a user

#### Cuisine Page (admin only)
* Add cuisine button links to add cuisine page
* For loop reveals all cuisines in the database
* Edit button links to edit cuisine page
* Delete button removes cuisine from database
* Delete modal to confirm removal of an item

#### Add Cuisine Page (admin only)
* Input for cuisine name
* Confirmation button linked to modal
* Cancel button returns user to cuisine page
* Modal adds new cuisine to database

#### Edit Cuisine Page (admin only)
* Input field shows existing data
* Confirmation button linked to confirmation modal
* Cancel button returns user to cuisine page
* Modal to confirm update of a cuisine

<a name="future"></a>

#### Future Features

* I currently only have one administrator and any restricted areas are accessed via username matching.
I would like to introduce multiple administrators via a dedicated is_admin field. I currently have added an 
is_admin field to the user database but due to time constraints have not written the code to use it as the 
key to access restricted pages. 

* I would like to add a filter system to select recipes based on other features. For example dietary 
requirements or cook times.

* I would like to add a review system so that users can review other peoples recipes and rate them.
___

<a name="test"></a>

### Testing

For all testing, please follow the link to a dedicated page. [Testing Page](testing.md) 
___

<a name="deploy"></a>

### Deployment

<a name="deploy"></a>

#### To deploy to heroku:
1. Create an app in heroku
2. In the config vars, add IP, Port, db uri and sectret key
3. Create and fill a requirements.txt file using python -m pip freeze
4. Change settings to debug = False in app.py
5. Ensure env.py is included in gitignore file
6. Remove import env from the app.py
7. Code is pushed to github
8. In heroku, set to the github deployment method for automatic updates 
9. To deploy click enable automatic deploys.  

<a name="run"></a>

#### To run this project locally:
You will need a github account and to use the chrome browser
1. Install the Github browser extensions for chrome, restart after installation
2. Login to gihub
3. Navigate to the project repository
4. Click on the "Gitpod" button, located in the top right of the page menu
5. This creates a new workspace for local workspace
6. In gitppd, create env.py file with the following contents:
  * os.environ.setdefault("IP", "0.0.0.0")
  * os.environ.setdefault("PORT", "5000")
  * os.environ.setdefault("SECRET_KEY", <>)
  * os.environ.setdefault("MONGO_URI", "mongodb+srv://domSpears:<>@myfirstcluster.7ycsu.mongodb.net/recipe_book?retryWrites=true&w=majority")
  * os.environ.setdefault("MONGO_DBNAME", "recipe_book")

<a name="clone"></a>

#### To clone this project (work within a local IDE)
1. Select the repository from githib
2. On the project page, click on the "code" dropdown menu icon
3. Copy the clone url by clicking the clipboard icon on the right side
4. Open git bash
5. Change wroking direcory to location where you want directory to be clones
5. Type git clone then paste the copied url
6. Press enter, the local clone is created
___

<a name="credit"></a>

### Credits

<a name="code"></a>

#### Code
* Force edit and delete buttons of recipes to the bottom of the div. [w3schools](https://www.w3schools.com/cssref/pr_pos_bottom.asp)

* Writing an if statment used for page authentication. [w3schools](https://www.w3schools.com/python/python_conditions.asp)

* How to make an input field accept a url (for recipe/cookware images). [w3schools](https://www.w3schools.com/tags/att_input_type_url.asp)

* Understanding how to add a customer number of ingredients/method steps. Mentor guidance.

* Create a new page to prevent the page position changing after a search. Mentor guidance.

* Understand the css grid and how to make divs responsive. [materialize](https://materializecss.com/grid.html)

* Learn how to capitalise the username on the profile page. [w3schools](https://www.w3schools.com/cssref/pr_text_text-transform.asp)

* Allow website links to be created in a new tab. [css-tricks](https://css-tricks.com/snippets/html/open-link-in-a-new-window/)

* Helped me understand jinja loops and statments [Codeburst](https://codeburst.io/jinja-2-explained-in-5-minutes-88548486834e) 

* Build a for loop of recipe cards. [Home assistant](https://community.home-assistant.io/t/build-cards-with-for-loop/212311)

<a name="media"></a>

#### Media

##### Images
* Recipe images were taken from the BBC food website.
* Cookware images were taken from the Greenpan website, mayflower collection.
* All other images were located via bing images, searched under "free to share and use" licences.

##### Content
* Recipe content (ingredients, method, e.t.c.) was taken from the BBC food website.
* Cookware content (prices, names e.t.c.) was taken from the the Greenpan cookware website.

<a name="acknowledgements"></a>

#### Acknowledgements

* Inspired by [W3Schools.com](https://www.w3schools.com/html/html_intro.asp)
General reference / tutorial assistance.

* Inspired by [Materialize.com](https://materializecss.com/)
General reference / tutorial assistance.

* Inspired by [BBC Food](https://www.bbc.co.uk/food)
General reference, inspiration.

* Inspired by [Code Institute Backend Mini Project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/054c3813e82e4195b5a4d8cd8a99ebaa/)
General reference, inspiration.

* Guido Cecilio (mentor) for offering guidance and support.
___