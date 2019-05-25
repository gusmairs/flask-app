from flask import Flask, render_template
import pandas as pd

app = Flask(__name__, static_url_path='')

contacts = pd.read_csv('names.txt')
records = contacts.to_dict(orient='records')
t = contacts.to_html(border=0, index=False, escape=True)
t.split('\n')

@app.route('/')
def index():
    return render_template('index.html',
                           message='Hello, my friend!',
                           table=t)
