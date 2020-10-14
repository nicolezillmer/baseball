from flask import Flask, render_template, redirect
from  flask_pymongo import PyMongo
#import scrapy

 # Flask Setup Flask Routes
app = Flask(__Farm__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/MLB_app"
mongo = PyMongo(app)
# create route that renders index.html template
@app.route("/")
def Home():
    Farm=mongo.db.Farm.find_one()
    # render_template("index.html", mlbFarm=mlbFarm)
    
"""List all available API routes."""
    
    return (
        f"Available Routes:<br/>"
        f"Welcome to your MLB Farm to Franchise Dashboard!:<br/>"
        f"/api/v1.0/about<br/>"
        f"/api/v1.0/visualization1<br/>"
        f"/api/v1.0/comparisons1<br/>"
        f"/api/v1.0/data1<br/>"
        f"/api/v1.0/contact"
    )

@app.route(“/api/v1.0/about”)
def about():
       Name = “Farm To Franchise, LLC”
       Location = “Arizona”
       Return f “We are {name} and we are located in - It’s a dry heat, {location}!”

@app.rout(“/api/v1.0/contact”)
def contact():
        Email = contact@FarmToFranchise.com
        Return f”Questions, Comments, Complaings? Send and email to {email}. Thanks!”

if __name__ == "__main__":
    app.run(debug=True)