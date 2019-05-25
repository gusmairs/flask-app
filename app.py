# import os
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__, static_url_path='')

# contacts = []
# with open('names.txt', 'r') as names:
#     contacts = names.read().splitlines()

contacts = pd.read_csv('names.txt')
records = contacts.to_dict(orient='records')
records

@app.route('/')
def index():
    return render_template('index.html',
                           message='Hello, my friend!',
                           records=records)
