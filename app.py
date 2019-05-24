# import os
from flask import Flask, render_template

app = Flask(__name__)

contacts = []
with open('names.txt', 'r') as names:
    contacts = names.read().splitlines()
print(contacts)

@app.route('/')
def index():
    return render_template('index.html',
                           message='Hello, my friend!',
                           contacts=contacts)
