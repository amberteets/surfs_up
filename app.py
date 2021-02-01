from flask import Flask

# Create new Flask app instance
app = Flask(__name__)

# Create Flask routes
## Define root (starting point)
@app.route('/')
### Code for specific route goes below root route
def hello_world():
    return 'Hello World'