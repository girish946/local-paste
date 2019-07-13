#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from peewee import SqliteDatabase

# init flask app
app = Flask(__name__)
api = Api(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
config = {"DB_FILE": "db/localPaste.db", "db": None, "admin_session": None}


def getDb():
    config["db"] = SqliteDatabase(config["DB_FILE"])
