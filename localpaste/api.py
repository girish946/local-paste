#!/usr/bin/python
# -*- coding: utf-8 -*-

from dbconnect import (createTables, insertPaste, selectDb,
                       deletePaste, updatePaste, selectPaste,
                       searchPaste)
from flask import request
from flask_restful import Resource


class DbInit(Resource):
    def get(self):
        if createTables():
            return {"CreateDb": "Success"}
        else:
            return {"CreateDb": "Failed"}


class NewPaste(Resource):
    def put(self):
        name = request.json['name']
        content = request.json['content']

        insertPaste(name=name,
                    content=content,
                    filename=name+'.txt')
        return {"insert": "success"}


class DeletePaste(Resource):
    def delete(self, pasteId):
        if deletePaste(pasteId=pasteId):
            return {"delete": "success"}
        else:
            return {"delete": "Failed"}


class UpdatePaste(Resource):
    def put(self, pasteId):
        name = request.json['name']
        content = request.json['content']
        # print(name, content)
        updatePaste(pasteId=pasteId, pasteName=name,
                    pasteContent=content, fileName=name+".txt",
                    debug=True)
        return {"ok": "done"}


class GetPaste(Resource):
    def get(self, pasteId):
        paste = [i for i in selectPaste(pasteId=pasteId)][0]
        return {"Name": paste.Name, "Id": paste.Id.hex,
                "Content": paste.Content,
                "TimeStamp": paste.TimeStamp.strftime("%b %d %Y %H:%M:%S")}


class SearchPaste(Resource):
    def get(self, keyword=None):
        pastes = [{"Id": i.Id.hex, "Name": i.Name,
                   "Content": i.Content,
                   "TimeStamp": i.TimeStamp.strftime("%b %d %Y %H:%M:%S")
                   }
                  for i in searchPaste(keyword=keyword)
                  ]
        return {keyword: pastes}

    def post(self):
        keyword = request.form['keyword']
        return self.get(keyword=keyword)


class SelectDb(Resource):
    def get(self):
        pastes = [{"Id": i.Id.hex, "Name": i.Name,
                   "Content": i.Content,
                   "TimeStamp": i.TimeStamp.strftime("%b %d %Y %H:%M:%S")
                   }
                  for i in selectDb(limit=0)
                  ]
        return {"pastes": pastes}
