#!/usr/bin/env python

# Flask app here drives the web site using a file-based sqlite database that
# does not sit in this repo. The sqlite3 parameter substitution method uses '?'
# placeholders with a tuple following the query string.

# The app renders the HTML table here on the server side using the convenience
# of the pandas::df.to_html() method.

from flask import (
    Flask, request, render_template, jsonify
)
import pandas as pd
import sqlite3 as sql

app = Flask(__name__, static_url_path='')

db = '/Users/gusmairs/OneDrive/DS_Study/flask-app/data/flask.db'
con = sql.connect(db)
c = con.cursor()

def get_table():
    qry = '''
        select rowid, name, age from names
        order by age desc
        ;
    '''
    dat = c.execute(qry)
    names_df = pd.DataFrame(
        dat.fetchall(),
        columns=['id', 'name', 'age']
    )
    tbl = names_df.loc[:, ['id', 'name', 'age']].to_html(border=0, index=False)
    return tbl

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show', methods=['GET'])
def show_table():
    return jsonify({'table': get_table()})

@app.route('/add', methods=['POST'])
def add_data():
    qry = '''
        insert into names values (?, ?)
        ;
    '''
    nm, ag = request.json['name'], request.json['age']
    c.execute(qry, (nm, ag))
    con.commit()
    return jsonify({'table': get_table()})

@app.route('/detail', methods=['POST'])
def get_detail():
    qry = '''
        select name from names where rowid = ?
        ;
    '''
    id = request.json['id']
    n = c.execute(qry, (id, ))
    name = n.fetchall()
    return jsonify({'name': name})
