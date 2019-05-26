from flask import Flask, request, render_template, jsonify
import pandas as pd

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    contacts = pd.read_csv('names.txt')
    t = contacts.to_html(border=0, index=False, escape=True)
    return render_template('index.html',
                           message='Hello, my friend!',
                           table=t)

@app.route('/add', methods=['POST'])
def add_name():
    name, age = (request.json['name'], request.json['age'])
    with open('names.txt', 'a') as file:
        file.write(name + ',' + age + '\n')
    contacts = pd.read_csv('names.txt')
    t = contacts.to_html(border=0, index=False, escape=True)
    return jsonify({'table': t})
    # return render_template('index.html',
    #                        message='New name added.',
    #                        table=t)
