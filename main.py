#! python3
# -*- coding: utf-8 -*-

from flask import Flask, flash, redirect, render_template, request
from flask import make_response
from api import *
from app_global import app, config
import argparse
import os


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
    return render_template("index.html")


@app.route("/login")
def showLogin():
    return render_template("login.html", Title="Login")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--db", help="the db file", type=str)
    arg = parser.parse_args()
    # print(arg.db)
    if arg.db and arg.db.endswith(".db"):
        print("swithing db to", arg.db)
        if os.path.exists(arg.db):
            print("file exists")
            config["DB_FILE"] = arg.db
        print(config)
    app.run(host="0.0.0.0", debug=True)
