#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from peewee import SqliteDatabase

# init flask app
app = Flask(__name__)
api = Api(app)

config = {
    "DB_FILE": 'localPaste.db',
    "db": None,
}

def getDb():
    config['db'] = SqliteDatabase(config["DB_FILE"])
