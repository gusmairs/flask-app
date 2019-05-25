from flask import Flask, render_template
import pandas as pd

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    contacts = pd.read_csv('names.txt')
    t = contacts.to_html(border=0, index=False, escape=True)
    return render_template('index.html',
                           message='Hello, my friend!',
                           table=t)
