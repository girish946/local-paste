#!/usr/bin/python
# -*- coding: utf-8 -*-

from peewee import (SqliteDatabase, Model, CharField, UUIDField,
                    DateTimeField, IntegerField,)
from app_global import config
import datetime
import uuid


db = SqliteDatabase(config["DB_FILE"])


class LocalPaste(Model):
    class Meta:
        database = db


class Users(LocalPaste):
    username = CharField(unique=True)
    Password = CharField()


class Pastes(LocalPaste):

    Id = UUIDField(primary_key=True)
    Name = CharField()
    Content = CharField()
    FileName = CharField()
    TimeStamp = DateTimeField(default=datetime.datetime.now)
    Status = IntegerField(default=1)


def printPastes(pastes):
    for i in pastes:
        print(i.Id,  i.Name, i.Content, i.FileName, i.TimeStamp)


def createTables():
    try:
        db.connect()
        db.create_tables([Users, Pastes])
    except Exception as e:
        return False
    return True


def selectDb(limit=10, nolim=False, debug=False):
    try:
        if limit:
            allPastes = Pastes.select().where(
                        Pastes.Status == 1
                        ).order_by(
                        Pastes.TimeStamp.desc()
                        ).limit(limit)
        else:
            allPastes = Pastes.select().where(
                        Pastes.Status == 1
                        ).order_by(Pastes.TimeStamp.desc())
        if debug:
            printPastes(allPastes)
        return allPastes
    except Exception as e:
        return False


def selectPaste(pasteId=None, debug=False):
    try:
        p = Pastes.select().where(Pastes.Id == pasteId)
        if debug:
            printPastes(p)

        return p
    except Exception as e:
        if debug:
            print(e, e.message)
        return False


def insertPaste(name="Untiteled", content=None, filename=None):
    try:
        uid = uuid.uuid4()
        p = Pastes.create(Id=uid, Name=name, Content=content,
                          FileName=filename)
        p.save()
    except Exception as e:
        return False
    return True


def deletePaste(pasteId=None, debug=False):

    if pasteId:
        print("deleting ", pasteId)
        try:
            delPaste = Pastes.delete().where(Pastes.Id == pasteId).execute()
            if debug:
                printPastes(delPaste)

        except Exception as e:
            print(e)
            return False
    return True


def updatePaste(pasteId=None, delete=False,
                pasteName=None, pasteContent=None,
                fileName=None, debug=False):
    if pasteId:
        if not delete:
            try:
                pid = Pastes.update(Name=pasteName,
                                    Content=pasteContent,
                                    FileName=fileName,
                                    TimeStamp=datetime.datetime.now()
                                    ).where(
                                    Pastes.Id == pasteId
                                    ).execute()

                if pid:
                    print(pid)
            except Exception as e:
                print(e)
        else:
            try:
                pid = Pastes.update(Status=0).where(
                                    Pastes.Id == pasteId
                                    ).execute()
            except Exception as e:
                print(e)


def searchPaste(keyword=None, debug=False):
    if keyword:
        try:
            pastes = Pastes.select().order_by(Pastes.Id.desc()).where(
                                   (Pastes.Name.contains(keyword)) |
                                   (Pastes.Content.contains(keyword)))
            if debug:
                printPastes(pastes)
            return pastes
        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("action", nargs='?',
                        help="\
                        Action: [select, insert, search, createDb, delete]")
    parser.add_argument("--pasteId", default="1",
                        help="sets the pasteId for operation", type=int)
    parser.add_argument("--keyword", help="Keyword for searching", type=str)
    parser.add_argument("--name", help="PasteName", type=str)
    parser.add_argument("--content", help="PasteContent", type=str)
    parser.add_argument("--fileName", help="PasteFilename", type=str)
    parser.add_argument("--limit", help="Limit on select query",
                        type=int, default=0)

    arg = parser.parse_args()

    if arg.pasteId:
        if arg.action == 'select':
            selectPaste(pasteId=arg.pasteId, debug=True)
        if arg.action == 'delete':
            print(deletePaste(pasteId=arg.pasteId, debug=True))

    if arg.keyword:
        if arg.action == 'search':
            searchPaste(keyword=arg.keyword, debug=True)
    else:
        if arg.action == 'select':
            selectDb(limit=arg.limit, debug=True)

        if arg.action == 'insert':
            pn = "dummy Name"
            pc = "dummy Content"
            pf = "dummyFile.txt"
            if arg.name:
                pn = arg.name
            if arg.content:
                pc = arg.content
            if arg.fileName:
                pf = arg.fileName
            print(insertPaste(name=pn, content=pc, filename=pf))

        if arg.action == 'createDb':
            createTables()
