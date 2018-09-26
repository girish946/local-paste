#!/usr/bin/python
# -*- coding: utf-8 -*-

from app_global import app, api
from flask import request
from flask_restful import Resource
from dbconnect import (createTables, insertPaste, selectDb,
                       deletePaste, updatePaste, selectPaste,
                       searchPaste)
import time

class DbInit(Resource):
    def get(self):
        if CreateTables():
            return {"CreateDb":"Success"}
        else:
            return {"CreateDb":"Failed"}


class NewPaste(Resource):

    def put(self):
        name = request.json['name']
        content = request.json['content']

        insertPaste(name = name, 
                    content = content,
                    filename = name+'.txt')
        return {"insert":"success"}


class DeletePaste(Resource):

    def delete(self, pasteId):
        if deletePaste(pasteId=pasteId):
            return {"delete":"success"}
        else:
            return {"delete":"Failed"}


class UpdatePaste(Resource):
    def put(self, pasteId):
        name = request.json['name']
        content = request.json['content']
        # print(name, content)
        updatePaste(pasteId=pasteId, pasteName=name,
                    pasteContent=content, fileName=name+".txt",
                    debug=True)
        return {"ok":"done"}


class GetPaste(Resource):
    def get(self, pasteId):
        paste = [i for i in selectPaste(pasteId=pasteId)][0]
        return {"name":paste.Name, "Id": paste.Id.hex,
                "content":paste.Content, 
                "timestamp":paste.TimeStamp.strftime("%b %d %Y %H:%M:%S")}


class SearchPaste(Resource):
    def get(self, keyword):
        pastes = [{"Id": i.Id.hex, "Name": i.Name,
                   "Content": i.Content,
                   "TimeStamp": i.TimeStamp.strftime("%b %d %Y %H:%M:%S")
                   }
                     for i in searchPaste(keyword=keyword)
                  ]
        return {keyword: pastes}


class SelectDb(Resource):
    def get(self):
        pastes = [{"Id": i.Id.hex, "Name": i.Name,
                   "Content": i.Content,
                   "TimeStamp": i.TimeStamp.strftime("%b %d %Y %H:%M:%S")
                   }
                     for i in selectDb(limit=0)
                  ]
        return {"pastes": pastes}


api.add_resource(DbInit,      '/api/CreateDb')
api.add_resource(NewPaste,    '/api/new')
api.add_resource(DeletePaste, '/api/delete/<string:pasteId>')
api.add_resource(UpdatePaste, '/api/update/<string:pasteId>')
api.add_resource(GetPaste,    '/api/get/<string:pasteId>')
api.add_resource(SearchPaste, '/api/search/<string:keyword>')
api.add_resource(SelectDb,    '/api/selectDb')

