#!/usr/bin/env python3
"""
A simple flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    Render the 0-index.html template
    """
    return render_template('0-index.html')
