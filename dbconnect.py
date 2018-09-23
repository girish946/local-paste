#!/usr/bin/python
# -*- coding: utf-8 -*-
import app_global
import sqlite3
import time
import sys


def getConnection():
    """
    returns the db connection.
    """
    return sqlite3.connect(app_global.config["DB_FILE"])


def createDb(debug=False):
    """
    creates the db.
    """

    try:
        con = getConnection()
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE Pastes(Id INTEGER PRIMARY KEY, Name Text,\
                                             Content TEXT, FileName TEXT,\
                                             Time INT)")
        return True

    except sqlite3.OperationalError as oe:
        if debug:
            print(oe, " has Row count:",  getRowCount())
        return False


def getRowCount(debug=False):
    """
    returns the total number of records in the db.
    """

    try:
        con = getConnection()
        with con:
            cur = con.cursor()
            cur.execute("SELECT Count(*) FROM Pastes")
            rows = cur.fetchall()
            return rows[0][0]
    except sqlite3.OperationalError as oe:
        if debug:
            print(oe)
        if oe == "no such table":
            return False


def selectPaste(pasteId=0, values="*", debug=False):
    """
    returns given vlaue for the given record.
    """

    try:
        con = getConnection()
        query = "select {0} from Pastes where Id=?".format(values)
        with con:
            cur = con.cursor()
            cur.execute(query, (pasteId,))
            rows = cur.fetchall()
            if debug:
                for i in rows:
                    print(i)
            return rows
    except Exception as e:
        if debug:
            print(e)
        return False


def searchPaste(col="content", search=None, debug=False):
    """
    returns all of the pastes containing given keyword.
    """

    try:
        con = getConnection()
        query = "select * from Pastes where content like ? or name like ?"
        with con:
            cur = con.cursor()
            cur.execute(query, ('%'+search+'%', '%'+search+'%',))
            rows = cur.fetchall()
            if debug:
                for i in rows:
                    print(i)
            return rows
    except Exception as e:
        print(e)
        return False


def updatePaste(pasteId=0, content=None, debug=True):
    """
    updates the given content for the given pasteId in the database.
    """
    if content:
        query = "UPDATE Pastes SET content = ? WHERE  Id = ?;"
        try:
            con = getConnection()
            with con:
                cur = con.cursor()
                cur.execute(query, (content, pasteId))
                rows = cur.fetchall()
                if debug:
                    for i in rows:
                        print(i)
                return rows
        except Exception as e:
            print(e)
            return False
    else:
        return False


def selectDb(rowCount=10, selectAll=False, debug=False):
    """
    returns given number of latest records.
    """

    try:
        con = getConnection()
        with con:
            cur = con.cursor()
            if selectAll:
                cur.execute("select * from Pastes;")
            else:
                query = "SELECT * FROM Pastes LIMIT ? OFFSET (SELECT COUNT(*)\
                         FROM Pastes)-?;"
                cur.execute(query, (rowCount, rowCount,))

            rows = cur.fetchall()
            if debug:
                for i in rows:
                    print(i)
        return reversed(rows)

    except sqlite3.OperationalError as oe:
        if debug:
            print(oe)
        return False

    except Exception as e:
        if debug:
            print(e)
        return False


def insertDb(name, content, filename=None, timestamp=time.time(), debug=False):
    """
    inserts a new record with given name, content, filename and timestamp in
    the database.
    """

    if not filename:
        filename = name+str(time.time())+".paste"

    query = "INSERT INTO Pastes(name, content, filename, time) VALUES \
             ( ?, ?, ?, ?)"
    if debug:
        print("executting query: {0}".format(query))
    try:
        con = getConnection()
        with con:
            cur = con.cursor()
            cur.execute(query, (name, content, filename, timestamp))
        if debug:
            print("executed successfully")
        return True
    except Exception as e:
        if debug:
            print(e)
        return False


def insertTest():

    count = 0
    if getRowCount() >= 0:
        count = getRowCount()

    content = "test content {0}".format(count)
    name = "test name {0}".format(count)
    filename = "test file name {0}".format(count)
    timestamp = time.time()
    if insertDb(content, filename, filename=filename, timestamp=timestamp,
                debug=True):
        selectDb()
    else:
        createDb()
        insertDb(name, content, filename, timestamp)
        selectDb()


def deletePaste(pasteId=None, debug=True):
    """
    deletes the given paste.
    """
    if pasteId:
        query = 'DELETE FROM Pastes WHERE Id=?'
        try:
            con = getConnection()
            with con:
                cur = con.cursor()
                cur.execute(query, (pasteId,))
            if debug:
                print("executed successfully")
            return True
        except Exception as e:
            if debug:
                print(e)
            return False


if __name__ == '__main__':

    content = "Test content"
    t = time.time()

    if sys.argv[1] == 's':
        selectDb(debug=True)
    elif sys.argv[1] == 'a':
        createDb()
    elif sys.argv[1] == 'i':
        insertTest()
    elif sys.argv[1] == 'g':
        selectPaste(sys.argv[2], sys.argv[3], debug=True)
    elif sys.argv[1] == 'ss':
        searchPaste(search=sys.argv[3], debug=True)
    else:
        pass
