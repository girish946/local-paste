#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask

# init flask app
app = Flask(__name__)

config = {
    "DB_FILE": 'localPaste.db'
}
