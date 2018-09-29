#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api

# init flask app
app = Flask(__name__)
api = Api(app)

config = {
    "DB_FILE": 'localPaste.db'
}
