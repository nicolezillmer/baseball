
# import necessary libraries
import json
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, inspect, func
from sqlalchemy.orm import Session
import pandas as pd

#from config import userName, password
engine = create_engine(os.environ.get('DATABASE_URL', ''))

#engine = create_engine('postgres://jhrqcslvcarqyy:519d2c118396fd3600cfeb0d7857ec8f106960e2ec1ec86cc5960e4daec6ff12@ec2-52-203-165-126.compute-1.amazonaws.com:5432/d2debj6f2p02g6')

Base = automap_base()
Base.prepare(engine, reflect=True)

inspector = inspect(engine)
inspector.get_table_names()
#Baseball = Base.classes.baseball

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index_dlf.html")

@app.route("/api/<selection>")
def data(selection):

    if selection == "batters":
        battersQuery = "SELECT * from batters"
        battersDF = battersDF = pd.read_sql_query(battersQuery, engine)
        result = battersDF.to_json(orient="split")
        return result
    elif selection == "pitchers":
        pitchersQuery = "SELECT * from pitchers"
        pitchersDF = pitchersDF = pd.read_sql_query(pitchersQuery, engine)
        result = pitchersDF.to_json(orient="split")
        return result
    else:
        return jsonify ("error")

@app.route("/api/era")
def era():

    eraQuery = "SELECT * from pitching_country_era"
    eraDF = pd.read_sql_query(eraQuery, engine)
    result = eraDF.to_json(orient = "split")

    return result

@app.route("/api/whip")
def whip():

    whipQuery = "SELECT * from pitching_country_whip"
    whipDF = pd.read_sql_query(whipQuery, engine)
    result = whipDF.to_json(orient = "split")

    return result

@app.route("/about")
def about():
       name = "Farm To Franchise, LLC"
       location = "Arizona"
       return f"We are {name} and we are located in - It’s a dry heat, {location}!"

@app.route("/contact")
def contact():
        Email = contact@FarmToFranchise.com
        return f'Questions, Comments, Complaints? Send and email to {email}. Thanks!'

if __name__ == "__main__":
    app.run(debug=True)

