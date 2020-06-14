import requests as r

base_url = "http://localhost:5000/api/"

def testDb():
    res = r.get(f"{base_url}selectDb")
    assert res.json()

def testCreateDb():
    res = r.get(f"{base_url}CreateDb")
    assert res.json()

def testCreatePaste():
    res = r.put(f"{base_url}new",
                json ={"name":"Initial Paste", "content":"Welcome to LocalPaste"}
               )
    assert res.json()

if __name__ == '__main__':
    testDb()
    testCreateDb()
    testDb()
    testCreatePaste()
    testDb()
