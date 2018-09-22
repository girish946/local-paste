#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, flash, redirect, render_template, request
from flask import make_response
from dbconnect import *
from app_global import *

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


@app.route("/get/<pasteId>")
def getPasteId(pasteId):

    data = selectPaste(pasteId=pasteId, values="content", debug=True)
    #print("data", data)
    r = make_response(data[0][0])
    r.headers['Content-type'] = 'text/plain; charset=utf-8'
    return r


@app.route("/delete/<pasteId>")
def do_delete(pasteId):
	if pasteId:
		print("deleting :",pasteId)
		if deletePaste(pasteId):

			return redirect("/")
		else:
			return "paste not deleted"