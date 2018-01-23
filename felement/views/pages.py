import collections

from flask import abort
from flask import render_template

from felement import db


def index():
    return render_template('index.html')
