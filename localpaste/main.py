#! python3
# -*- coding: utf-8 -*-

from .api import (DbInit, NewPaste, DeletePaste,
                 UpdatePaste, GetPaste, SearchPaste,
                 SelectDb)
from flask import render_template
from .app_global import app, config, api, getDb
import argparse
import os


# This file is used for starting the application on the local machie and
# for rendering the Templates. For APIs see localpaste/api.py

@app.route("/showPaste/<pasteId>")
def showPost(pasteId):
    return render_template("view.html", pasteId=pasteId)


@app.route("/new")
def newPaste():
    return render_template("paste.html", Title="Create New Paste",
                           action="/makePaste")


@app.route("/pasteUpdate/<pasteId>")
def showUpdate(pasteId):
    return render_template("paste.html", Title="Create New Paste",
                           updatePaste=True, pasteId=pasteId,
                           action="/update")


@app.route("/search/")
def showSearch():
    return render_template("search.html", Title="Search")


@app.route("/")
def index():
    return render_template("index.html",  Title="Index")


@app.route("/login")
def showLogin():
    return render_template("login.html", Title="Login")


def addResources():

    # add the routes for all APIs.
    api.add_resource(DbInit,      '/api/CreateDb')
    api.add_resource(NewPaste,    '/api/new')
    api.add_resource(DeletePaste, '/api/delete/<string:pasteId>')
    api.add_resource(UpdatePaste, '/api/update/<string:pasteId>')
    api.add_resource(GetPaste,    '/api/get/<string:pasteId>')
    api.add_resource(SearchPaste, '/api/search', methods=['POST'],
                     endpoint='Search_post')
    api.add_resource(SearchPaste, '/api/search/<string:keyword>',
                     methods=['GET'], endpoint='Search_get')
    api.add_resource(SelectDb,    '/api/selectDb')


def startServer(host="0.0.0.0", port=5000):
    # Run the application.
    app.run(host=host, port=port, debug=True)

