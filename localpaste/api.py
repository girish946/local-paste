#!/usr/bin/python
# -*- coding: utf-8 -*-

from dbconnect import (createTables, insertPaste, selectDb,
                       deletePaste, updatePaste, selectPaste,
                       searchPaste)
from flask import request
from flask_restful import Resource


class DbInit(Resource):
    """
    This class is responsible for creating the dbatabase.
    The first thing to be done after setup is to create a db.
    """
    def get(self):
        if createTables():
            return {"CreateDb": "Success"}
        else:
            return {"CreateDb": "Failed"}


class NewPaste(Resource):
    """
    To create a new paste.
    curl --header "Content-Type: application/json" \
    --request PUT \
    --data '{"name": "Some PasteName", "content": "dummy Content"}' \
    http://localhost:5000/api/new
    """
    def put(self):
        name = request.json['name']
        content = request.json['content']

        insertPaste(name=name,
                    content=content,
                    filename=name+'.txt')
        return {"insert": "success"}


class DeletePaste(Resource):
    """
    To delete the paste.
    curl http://localhost:5000/api/delete/<pasteId> -X DELET
    """
    def delete(self, pasteId):
        """
        Only admin should be able to delete the paste.
        This will be implemented when users are created.
        if admin:
            if deletePaste(pasteId=pasteId):
                return {"delete": "success"}
            else:
                return {"delete": "Failed"}
        else:"""
        updatePaste(pasteId=pasteId, delete=True)
        return {"delete": "success"}


class UpdatePaste(Resource):
    """
    To update the paste Contents and name.
    curl --header "Content-Type: application/json" \
    --request PUT \
    --data '{"name": "New PasteName", "content": " newdummy Content"}' \
    http://localhost:5000/api/update/<pasteId>
    """
    def put(self, pasteId):
        name = request.json['name']
        content = request.json['content']
        # print(name, content)
        updatePaste(pasteId=pasteId, pasteName=name,
                    pasteContent=content, fileName=name+".txt",
                    debug=True)
        return {"ok": "done"}


class GetPaste(Resource):
    """
    To retrive a paste.
    curl http://localhost:5000/api/get/<pasteId>
    """
    def get(self, pasteId):
        paste = [i for i in selectPaste(pasteId=pasteId)][0]
        return {"Name": paste.Name, "Id": paste.Id.hex,
                "Content": paste.Content,
                "TimeStamp": paste.TimeStamp.strftime("%b %d %Y %H:%M:%S")}


class SearchPaste(Resource):
    """
    To search a keyword in the pastes.
    curl http://localhost:5000/api/search/<keyword>
    """
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
    """
    To retrive all pastes from the db.
    curl http://localhost:5000/api/selectDb
    """
    def get(self):
        pastes = [{"Id": i.Id.hex, "Name": i.Name,
                   "Content": i.Content,
                   "TimeStamp": i.TimeStamp.strftime("%b %d %Y %H:%M:%S")
                   }
                  for i in selectDb(limit=0)
                  ]
        return {"pastes": pastes}
