#!/usr/bin/env python

# Flask app here drives the web site using a MongoDB database that runs on a
# local server port. Note how simple the querying is through pymongo, with many
# lines of SQL query code eliminated and no parameter substitution into string
# queries needed.

# The app renders the HTML table here on the server side using the convenience
# of the pandas::df.to_html() method. To do: leave the data in .json format and
# send to the client for JavaScript to render into the table.

from flask import (
    Flask, request, render_template, jsonify
)
from bson.objectid import ObjectId
import pandas as pd
import pymongo

app = Flask(__name__, static_url_path='')

mongo = pymongo.MongoClient()
db = mongo['one_db']

def get_table():
    mg_dat = db.people.find().sort('age', -1)
    names_df = pd.DataFrame(list(mg_dat))
    tbl = names_df.loc[
        :,
        ['_id', 'name', 'age']
    ].to_html(border=0, index=False)
    return tbl

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show', methods=['GET'])
def show_table():
    return jsonify({'table': get_table()})

@app.route('/add', methods=['POST'])
def add_data():
    db.people.insert_one(request.json)
    return jsonify({'table': get_table()})

@app.route('/detail', methods=['POST'])
def get_detail():
    mg_one = db.people.find_one({'_id': ObjectId(request.json['id'])})
    return jsonify({'name': mg_one['name']})
