import requests as r

def testDb():
    res = r.get("http://localhost:5000/api/selectDb")
    assert res.json()

def testCreateDb():
    res = r.get("http://localhost:5000/api/CreateDb")
    assert res.json()

def testCreatePaste():
    res = r.put("http://localhost:5000/api/new",
                json ={"name":"Initial Paste", "content":"Welcome to LocalPaste"}
               )
    assert res.json()

if __name__ == '__main__':
    testDb()
    testCreateDb()
    testDb()
    testCreatePaste()
    testDb()
