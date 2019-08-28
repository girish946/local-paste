import requests as r

def testDb():
    res = r.get("http://0.0.0.0:8000/api/selectDb")
    print(res.json())

def testCreateDb():
    res = r.get("http://0.0.0.0:8000/api/CreateDb")
    print(res.json())

def testCreatePaste():
    res = r.put("http://0.0.0.0:8000/api/new",
                json ={"name":"Initial Paste", "content":"Welcome to LocalPaste"}
               )
    print(res.json())

if __name__ == '__main__':
    testDb()
    testCreateDb()
    testDb()
    testCreatePaste()
    testDb()
