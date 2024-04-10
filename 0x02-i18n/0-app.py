#!/usr/bin/env python3
'''Basic Flask app'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    '''calls render template on the html file'''
    return render_template('0-index.html')


app.run(debug=True)
