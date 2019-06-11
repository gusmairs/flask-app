from flask import Flask, request, render_template, jsonify
import pandas as pd
import pymongo

app = Flask(__name__, static_url_path='')

mongo = pymongo.MongoClient()
db = mongo['one_db']

def get_table():
    names_df = pd.DataFrame(list(db.people.find({}, {'_id': 0})))
    tbl = names_df[['name', 'age']].to_html(table_id='wowie',
                                            border=0, index=False)
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
