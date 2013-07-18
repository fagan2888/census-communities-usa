from flask import Flask,jsonify
import flask
import simplejson as json
import os
import sys
import pymongo
from urlparse import urlparse
from bson import Binary, Code
from bson.json_util import dumps

app = Flask(__name__)

#BAD MONGO URL
#NEVER DO THIS

@app.route("/state/<state>")
def get_state(state):
	return placeholder

@app.route("/year/<year>")
def get_year(year):
	return "you wanted a year"

@app.route("/get-all/<year>/<state>")
def get_year_and_state(year,state):
	return os.environ.get('MONGOHQ_URL')

@app.route("/residence-block/<int:block>")
def find_block(block):
	return "test"

@app.route("/")
def hello():
    return "Hello World, again"

if __name__ == "__main__":
	app.run(debug=True)