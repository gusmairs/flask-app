from flask import Flask, request, render_template, jsonify
import pandas as pd

app = Flask(__name__, static_url_path='')

def get_table():
    names_df = pd.read_csv('names.txt')
    tbl = names_df.to_html(border=0, index=False, escape=False)
    return tbl

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show', methods=['GET'])
def show_table():
    return jsonify({'table': get_table()})

@app.route('/add', methods=['POST'])
def add_data():
    name, age = (request.json['name'], request.json['age'])
    with open('names.txt', 'a') as file:
        file.write(name + ',' + age + '\n')
    return jsonify({'table': get_table()})
