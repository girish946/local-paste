#! python3
# -*- coding: utf-8 -*-

from flask import Flask, flash, redirect, render_template, request
from flask import make_response
from api import *
# from dbconnect import selectPaste, searchPaste, selectDb, getRowCount
from app_global import app, config
import argparse
import os


@app.route("/showPaste/<pasteId>")
def showPost(pasteId):
    return render_template("view.html", pasteId=pasteId)


"""@app.route("/new")
def newPaste():
    return render_template("paste.html", Title="Create New Paste",
                           action="/makePaste")


@app.route("/makeSearch/", methods=['POST'])
@app.route("/makeSearch/<keyword>", methods=['GET', 'POST'])
def makeSearch(keyword=None):
    # print(request.method)
    if keyword and request.method == 'GET':
        pastes = [{"Id": i[0], "name": i[1]}
                  for i in searchPaste(search=keyword)
                  ]

    elif not keyword and request.method == 'POST':
        # print("searching for", request.form["keyword"])
        pastes = [{"Id": i[0], "name": i[1]}
                  for i in searchPaste(search=request.form["keyword"])
                  ]
        title = "Search: {0}".format(keyword)
        # print(pastes)
        return render_template("index.html", pastes=pastes,
                               Title=title, more=True)
    else:
        return redirect("/search")


@app.route("/search/")
def showSearch():
    return render_template("search.html", Title="Search")"""


@app.route("/pasteUpdate/<pasteId>")
def showUpdate(pasteId):
    return render_template("paste.html", Title="Create New Paste",
                           updatePaste=True, pasteId=pasteId,
                           action="/update")


"""@app.route("/")
def index():
    rowCount = getRowCount()
    pastes = [{"Id": i[0], "name":i[1]}
              for i in selectDb(rowCount=10,
                                selectAll=True)
              ]
    title = "Pastes"
    if rowCount > 10:
        return render_template("index.html", pastes=pastes, Title=title,
                               more=True)
    else:
        return render_template("index.html", pastes=pastes, Title=title,
                               more=False)


@app.route("/login")
def showLogin():
    return render_template("login.html", Title="Login")"""

@app.route("/")
def index():
    return render_template("temp.html")

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
