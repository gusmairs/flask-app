from flask import Flask, request, render_template, jsonify
import pandas as pd
import sqlite3 as sql

app = Flask(__name__, static_url_path='')

db = '/Users/gusmairs/OneDrive/DS_Study/flask-app/data/flask.db'
con = sql.connect(db)
c = con.cursor()

def get_table():
    dat = c.execute('''
        select rowid, name, age from names
        order by age desc
        ;
        ''')
    names_df = pd.DataFrame(dat.fetchall(), columns=['id', 'name', 'age'])
    tbl = names_df[['id', 'name', 'age']].to_html(border=0, index=False)
    return tbl

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show', methods=['GET'])
def show_table():
    return jsonify({'table': get_table()})

@app.route('/add', methods=['POST'])
def add_data():
    c.execute('''
        insert into names values (?, ?)
        ;
        ''', (request.json['name'], request.json['age']))
    con.commit()
    return jsonify({'table': get_table()})

@app.route('/detail', methods=['POST'])
def get_detail():
    n = c.execute('''
        select name from names where rowid = ?
        ;
        ''', (request.json['id'], ))
    name = n.fetchall()
    return jsonify({'name': name})
