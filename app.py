# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine(os.environ.get('DATABASE_URL', ''))

Base = automap_base()
Base.prepare(engine, reflect=True)

Pet = Base.classes.pets

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("../index.html")


@app.route("/api/pals")
def pals():

    session = Session(engine)

    #results = db.session.query(Pet.name, Pet.lat, Pet.lon).all()
    results = session.query(Pet.name, Pet.lat, Pet.lon).all()

    hover_text = [result[0] for result in results]
    lat = [result[1] for result in results]
    lon = [result[2] for result in results]

    pet_data = [{
        "type": "scattergeo",
        "locationmode": "USA-states",
        "lat": lat,
        "lon": lon,
        "text": hover_text,
        "hoverinfo": "text",
        "marker": {
            "size": 50,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    session.close()

    return jsonify(pet_data)


if __name__ == "__main__":
    app.run()




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
       return f“We are {name} and we are located in - It’s a dry heat, {location}!”

@app.rout(“/api/v1.0/contact”)
def contact():
        Email = contact@FarmToFranchise.com
        Return f”Questions, Comments, Complaings? Send and email to {email}. Thanks!”

if __name__ == "__main__":
    app.run(debug=True)