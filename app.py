# Import Dependencies
## Python Dependencies
import datetime as dt
import numpy as np
import pandas as pd
## SQLAlchemy Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
## Flask Dependencies
from flask import Flask, jsonify

# Set up database engine
engine = create_engine("sqlite:///hawaii.sqlite")
# Reflect database/tables into classes
Base = automap_base()
Base.prepare(engine, reflect=True)
# Create variables for each class
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create session link from Python to database
session = Session(engine)

# Set up Flask
## Create Flask application 
app = Flask(__name__)
## Define root ('welcome route')
@app.route('/')

# Welcome function
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():

    # Calculate date 1 year prior to most recent date in database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query for date/precipitation for previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()

    # Create dictionary with key=date, value=precipitation
    precip = {date: prcp for date, prcp in precipitation}

    # Return 'JSONified' version of precip dictionary
    return jsonify(precip)

# Stations Route
@app.route("/api/v1.0/stations")
def stations():
    
    # Query for all stations 
    results = session.query(Station.station).all()

    # Unravel results to 1-D array using numpy function .ravel(); convert to list
    stations = list(np.ravel(results))

    # Return 'JSONified' version of stations
    return jsonify(stations=stations)