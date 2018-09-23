#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, flash, redirect, render_template, request
from flask import make_response
from dbconnect import *
from app_global import *

@app.route("/makePaste", methods=['POST'])
def do_paste():
    name    = request.form['PasteName']
    content = request.form['PasteContent']
    if not name:
        name = "untiteled"
    if insertDb(name, content, name):
        return redirect("/")
    else:
        return redirect("/")


@app.route("/get/<pasteId>")
def do_get(pasteId):

    data = selectPaste(pasteId=pasteId, values="content")
    #print("data", data)
    r = make_response(data[0][0])
    r.headers['Content-type'] = 'text/plain; charset=utf-8'
    return r

@app.route("/update", methods=["POST"])
def do_update():
    pasteId = request.form['PasteId']
    content = request.form['PasteContent']
    result = updatePaste(pasteId=pasteId, content=content)    
    return redirect("/")

@app.route("/delete/<pasteId>")
def do_delete(pasteId):
	if pasteId:
		#print("deleting :",pasteId)
		if deletePaste(pasteId):

			return redirect("/")
		else:
			return "paste not deleted"