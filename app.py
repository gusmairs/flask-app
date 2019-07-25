from flask import Flask, request, render_template, jsonify
from bson.objectid import ObjectId
import pandas as pd
import sqlite3 as sql
# import pymongo


app = Flask(__name__, static_url_path='')

# mongo = pymongo.MongoClient()
# db = mongo['one_db']
db = 'flask.db'

def get_table():
    con = sql.connect(db)
    c = con.cursor()
    dat = c.execute('''
        select name, age from names
        ;
        ''')
    # mg_dat = db.people.find().sort('age', -1)
    names_df = pd.DataFrame(dat.fetchall(), columns=['name', 'age'])
    # names_df = pd.DataFrame(list(mg_dat))
    tbl = names_df[['name', 'age']].to_html(border=0, index=False)
    con.close()
    return tbl

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show', methods=['GET'])
def show_table():
    return jsonify({'table': get_table()})

@app.route('/add', methods=['POST'])
def add_data():
    print(request.json['name'], request.json['age'])
    con = sql.connect(db)
    c = con.cursor()
    c.execute('''
        insert into names values (?, ?)
        ;
        ''', (request.json['name'], request.json['age']))
    con.commit()
    con.close()
    # db.people.insert_one(request.json)
    return jsonify({'table': get_table()})

@app.route('/detail', methods=['POST'])
def get_detail():
    mg_one = db.people.find_one({'_id': ObjectId(request.json['id'])})
    return jsonify({'name': mg_one['name']})
