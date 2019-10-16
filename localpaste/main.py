#! python3
# -*- coding: utf-8 -*-

from .api import (
    DbInit,
    NewPaste,
    DeletePaste,
    UpdatePaste,
    GetPaste,
    RecordCount,
    SearchPaste,
    SelectNextX,
    SelectDb,
    UserLogin,
    UserLogout,
)
from .dbconnect import selectPaste
from flask import render_template, redirect, session
from .app_global import app, config, api, getDb


# This file is used for starting the application on the local machie and
# for rendering the Templates. For APIs see localpaste/api.py


@app.route("/showPaste/<pasteId>")
def showPost(pasteId):
    paste = [i for i in selectPaste(pasteId=pasteId)]
    if paste:
        data = {
            "Status": "Success",
            "Name": paste[0].Name,
            "Id": paste[0].Id.hex,
            "Content": paste[0].Content,
        }
        return render_template(
            "view.html", Title=data["Name"], pasteId=pasteId, data=data
        )
    data = {"Status":{"Error": "No such paste"},
            "Content": None,
            "Name": None}
    return render_template(
        "view.html", Title="No such paste", pasteId=pasteId, data=data)


@app.route("/new")
def newPaste():
    return render_template("paste.html", Title="Create New Paste", action="/makePaste")


@app.route("/pasteUpdate/<pasteId>")
def showUpdate(pasteId):
    return render_template(
        "paste.html",
        Title="Create New Paste",
        updatePaste=True,
        pasteId=pasteId,
        action="/update",
    )


@app.route("/search/")
def showSearch():
    return render_template("search.html", Title="Search")


@app.route("/")
def index():
    return render_template("index.html", Title="Index", Limit=10, Offset=0)


@app.route("/login")
def showLogin():
    return render_template("login.html", Title="Login")


@app.route("/logout")
def doLogout():
    if "username" in session:
        session.pop("username")
        config.pop("admin_session")
        # print(session)
        # print(config)
    return redirect("/")


def addResources():

    # add the routes for all APIs.
    api.add_resource(DbInit, "/api/CreateDb")
    api.add_resource(NewPaste, "/api/new")
    api.add_resource(RecordCount, "/api/recordCount")
    api.add_resource(DeletePaste, "/api/delete/<string:pasteId>")
    api.add_resource(UpdatePaste, "/api/update/<string:pasteId>")
    api.add_resource(GetPaste, "/api/get/<string:pasteId>")
    api.add_resource(
        SearchPaste, "/api/search", methods=["POST"], endpoint="Search_post"
    )
    api.add_resource(
        SearchPaste,
        "/api/search/<string:keyword>",
        methods=["GET"],
        endpoint="Search_get",
    )
    api.add_resource(SelectDb, "/api/selectDb")
    api.add_resource(SelectNextX, "/api/selectNextX/<int:limit>/<int:offset>")
    api.add_resource(UserLogin, "/api/login")
    api.add_resource(UserLogout, "/api/logout")


def startServer(host="0.0.0.0", port=5000):
    # Run the application.
    app.run(host=host, port=port)
