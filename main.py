#! python3

from flask import Flask, flash, redirect, render_template, request
from flask import make_response
from dbconnect import *


app = Flask(__name__)


@app.route("/makePaste", methods=['POST'])
def makePaste():
    name    = request.form['PasteName']
    content = request.form['PasteContent']
    if not name:
        name = "untiteled"
    if insertDb(name, content, name, debug=True):
        return redirect("/")
    else:
        return redirect("/")


@app.route("/showPaste/<pasteId>")
def showPost(pasteId, values="name"):

    data = selectPaste(pasteId, values="name") 
    return render_template("view.html", pasteId=pasteId, Title=data[0][0])

@app.route("/get/<pasteId>")
def getPasteId(pasteId):

    data = selectPaste(pasteId, values="content")
    r = make_response(data[0][0])
    r.headers['Content-type'] = 'text/plain; charset=utf-8'
    return r


@app.route("/new")
def newPaste():
    return render_template("paste.html", Title="Create New Paste")


@app.route("/")
def index():
    rowCount = getRowCount()
    pastes = [{"Id":i[0], "name":i[1]} for i in selectDb(rowCount=10, selectAll=True)]
    title  = "Pastes"
    if rowCount>10:
        return render_template("index.html", pastes=pastes, Title=title, more=True)
    else:
        return render_template("index.html", pastes=pastes, Title=title, more=False)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
