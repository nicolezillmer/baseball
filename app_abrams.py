# import necessary libraries
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

from config import userName, password

#engine = create_engine(os.environ.get('DATABASE_URL', ''))
engine = create_engine(f'postgresql://{userName}:{password}@localhost:5432/baseball')


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
    return render_template("index_abrams.html")

'''
@app.route("/api/<name>")
def player(name):

    session = Session(engine)

    #results = db.session.query(Pet.name, Pet.lat, Pet.lon).all()
    #results = session.query(Pet.name, Pet.lat, Pet.lon).all()



    session.close()

    return jsonify()
'''

@app.route("/about")
def about():
       name = "Farm To Franchise, LLC"
       location = "Arizona"
       return f"We are {name} and we are located in - It’s a dry heat, {location}!"

@app.route("/contact")
def contact():
        Email = contact@FarmToFranchise.com
        return f'Questions, Comments, Complaings? Send and email to {email}. Thanks!'

if __name__ == "__main__":
    app.run(debug=True)