#! python3

from flask import Flask, flash, redirect, render_template, request
from flask import make_response
from dbconnect import *
from app_global import *

#app = Flask(__name__)


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
@app.route("/makeSearch/", methods=['POST'])
@app.route("/makeSearch/<keyword>", methods=['GET', 'POST'])
def makeSearch(keyword=None):
    print(request.method)
    if keyword and request.method == 'GET':
        pastes = [{"Id":i[0], "name":i[1]} for i in searchPaste(search=keyword)]
    elif not keyword and request.method == 'POST':
        print("searching for", request.form["keyword"])
        pastes = [{"Id":i[0], "name":i[1]} for i in searchPaste(search=request.form["keyword"])]
        title  = "Search: {0}".format(keyword)
        print(pastes)
        return render_template("index.html", pastes=pastes, Title=title, more=True)
    else:
        return redirect("/search")

@app.route("/search/")
def showSearch():
    return render_template("search.html", Title="Search")

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
    app.run(host="0.0.0.0", debug=True)
