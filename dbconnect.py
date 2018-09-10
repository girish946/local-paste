#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 
import time
import sys

def getConnection():
    return sqlite3.connect('test.db')

def createDb(debug=False):
    try:
        con = getConnection()
        with con:    
            cur = con.cursor()    
            cur.execute("CREATE TABLE Pastes(Id INT, Name Text, Content TEXT,\
                                             FileName TEXT, Time INT)")
        return True

    except sqlite3.OperationalError as oe:
        if debug:
            print(oe," has Row count:",  getRowCount())
        return False


def getRowCount(debug=False):
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
    try:
        con = getConnection()
        with con:
            cur = con.cursor()
            cur.execute("select {0} from Pastes where Id={1};".format(values,
                                                                      pasteId))
            rows = cur.fetchall()
            if debug:
                for i in rows:
                    print(i)
            return rows
    except Exception as e:
        return False

def selectDb(rowCount=10, selectAll=False,debug=False):
    try:
        con = getConnection()
        with con:
            cur = con.cursor()
            if selectAll:
                cur.execute("select * from Pastes;")    
            else:
                query = "SELECT * FROM Pastes LIMIT {0} OFFSET (SELECT COUNT(*) FROM Pastes)-{0};".format(rowCount)
                cur.execute(query)

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
    if not filename:
        filename = name+str(time.time())+".paste"
    if getRowCount():
        pasteId = getRowCount() + 1
    else:
        pasteId = 0
    query = "INSERT INTO Pastes VALUES(?, ?, ?, ?, ?);"
    if debug:
        print("executting query: {0}".format(query))
    try:
        con = getConnection()
        with con:
            cur = con.cursor()
            cur.execute(query,(pasteId, name, content, filename, timestamp,))
        if debug:
            print("executed successfully")
        return True
    except Exception as e:
        if debug:
            print(e)
        return False

def insertTest():

    count = 0
    if getRowCount():
        count = getRowCount()
    print(count)
    content   = "test content {0}".format(count)
    name      = "test name {0}".format(count)
    filename  = "test file name {0}".format(count)
    timestamp = time.time()
    if insertDb(content, filename, timestamp):
        selectDb()
    else:
        createDb()
        insertDb(name, content, filename, timestamp)
        selectDb()



if __name__ == '__main__':

    #con = sqlite3.connect('test.db')
    content = "Test content"
    t = time.time()

    if sys.argv[1] == 's':
        selectDb(debug=True)
    elif sys.argv[1] == 'a':
        createDb()
    elif sys.argv[1] =='i':
        insertTest()
    elif sys.argv[1] == 'g':
        selectPaste(sys.argv[2], sys.argv[3], debug=True)
    else:
        pass
