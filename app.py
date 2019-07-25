from flask import Flask, request, render_template, jsonify
import pandas as pd
import sqlite3 as sql


app = Flask(__name__, static_url_path='')

db = 'flask.db'

def get_table():
    con = sql.connect(db)
    c = con.cursor()
    dat = c.execute('''
        select rowid, name, age from names
        order by age desc
        ;
        ''')
    names_df = pd.DataFrame(dat.fetchall(), columns=['id', 'name', 'age'])
    tbl = names_df[['id', 'name', 'age']].to_html(border=0, index=False)
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
    con = sql.connect(db)
    c = con.cursor()
    c.execute('''
        insert into names values (?, ?)
        ;
        ''', (request.json['name'], request.json['age']))
    con.commit()
    con.close()
    return jsonify({'table': get_table()})

@app.route('/detail', methods=['POST'])
def get_detail():
    con = sql.connect(db)
    c = con.cursor()
    n = c.execute('''
        select name from names where rowid = ?
        ;
        ''', (request.json['id'], ))
    name = n.fetchall()
    con.close()
    return jsonify({'name': name})
