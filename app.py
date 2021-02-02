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