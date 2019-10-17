#!/usr/bin/python
# -*- coding: utf-8 -*-

from .dbconnect import (
    createTables,
    insertPaste,
    selectDb,
    getRecordCount,
    deletePaste,
    updatePaste,
    selectPaste,
    searchPaste,
    getLogin,
)
from flask import request, session
from flask_restful import Resource
from .app_global import config


class DbInit(Resource):
    """
    This class is responsible for creating the dbatabase.
    The first thing to be done after setup is to create a db.
    """

    def get(self):
        if createTables():
            return {"CreateDb": "Success"}
        return {"CreateDb": "Failed"}


class RecordCount(Resource):
    def get(self):
        try:
            count = getRecordCount()
            if count != -1:
                return {"count": count}
            return {"error": "Something went wrong"}
        except Exception as e:
            return {"error": "No table pastes"}


class NewPaste(Resource):
    """
    To create a new paste.
    curl --header "Content-Type: application/json" \
    --request PUT \
    --data '{"name": "Some PasteName", "content": "dummy Content"}' \
    http://localhost:5000/api/new
    """

    def put(self):
        name = request.json["name"]
        content = request.json["content"]

        insertPaste(name=name, content=content, filename=name + ".txt")
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
        name = request.json["name"]
        content = request.json["content"]
        # print(name, content)
        updatePaste(
            pasteId=pasteId,
            pasteName=name,
            pasteContent=content,
            fileName=name + ".txt",
            debug=True,
        )
        return {"ok": "done"}


class GetPaste(Resource):
    """
    To retrive a paste.
    curl http://localhost:5000/api/get/<pasteId>
    """

    def get(self, pasteId):
        paste = [i for i in selectPaste(pasteId=pasteId)]
        if paste:
            return {
                "Name": paste[0].Name,
                "Id": paste[0].Id.hex,
                "Content": paste[0].Content,
                "TimeStamp": paste[0].TimeStamp.strftime("%b %d %Y %H:%M:%S"),
            }
        return {"Error": "No such paste"}


class SearchPaste(Resource):
    """
    To search a keyword in the pastes.
    curl http://localhost:5000/api/search/<keyword>
    """

    def get(self, keyword=None):
        pastes = [
            {
                "Id": i.Id.hex,
                "Name": i.Name,
                "Content": i.Content,
                "TimeStamp": i.TimeStamp.strftime("%b %d %Y %H:%M:%S"),
            }
            for i in searchPaste(keyword=keyword)
        ]
        return {keyword: pastes}

    def post(self):
        keyword = request.form["keyword"]
        return self.get(keyword=keyword)


class SelectNextX(Resource):
    """
    To select the next x pastes. The default is 10
    """

    def get(self, limit=10, offset=0):
        try:
            pastes = [
                {
                    "Id": i.Id.hex,
                    "Name": i.Name,
                    "Content": i.Content,
                    "TimeStamp": i.TimeStamp.strftime("%b %d %Y %H:%M:%S"),
                }
                for i in selectDb(limit=limit, offset=offset)
            ]
            return {"pastes": pastes}
        except Exception as e:
            return {"Error": str(e)}


class SelectDb(Resource):
    """
    To retrive all pastes from the db.
    curl http://localhost:5000/api/selectDb
    """

    def get(self):
        try:
            pastes = [
                {
                    "Id": i.Id.hex,
                    "Name": i.Name,
                    "Content": i.Content,
                    "TimeStamp": i.TimeStamp.strftime("%b %d %Y %H:%M:%S"),
                }
                for i in selectDb(limit=0)
            ]
            return {"pastes": pastes}
        except Exception as e:
            return {"Error": str(e)}


class UserLogin(Resource):
    """
    user login
    """

    def post(self):
        # print(request.json)
        if "username" in request.json:
            username = request.json["username"]
            if "password" in request.json:
                password = request.json["password"]
                # print(request.json)
                if getLogin(username, password):
                    session["username"] = username
                    session["token"] = config["admin_session"]
                    return {"login": "success", "token": config["admin_session"]}
        return {"login": "failed"}


class UserLogout(Resource):
    """
    user logout
    """

    def get(self):
        if "username" in session:
            session.pop("username")
            config.pop("admin_session")
            print(session)
            print(config)
            return {"logout": "success"}
        return {"logout": "failed"}
