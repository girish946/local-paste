import argparse
import requests

parser = argparse.ArgumentParser()
debug = 0

url = "http://{0}:{1}/"


def GetPaste(pasteId):
    print(pasteId)
    r = requests.get(url+"api/get/"+pasteId)
    print(r.text)


def AddNewPaste(pasteName, pasteContent):
    pasteDetails = {'name': pasteName, 'content': pasteContent}
    r = requests.put(url+"api/new", json=pasteDetails)
    if r.status_code == 200:
        print(r.content)
    else:
        print("error")


def UpdateAPaste(pasteId, pasteContent,append):
    req = requests.get(url+"api/get/"+pasteId)
    details=req.json()    
    
    
    if pasteContent:
        if append != True:
            contentToUpdate=pasteContent
        else:
            contentToUpdate=details['Content']+" "+pasteContent 
        pasteDetails = {'name': details['Name'], 'content': contentToUpdate}         
        r=requests.put(url+"/api/update/"+pasteId,json=pasteDetails)
       


def DeleteAPaste(pasteId):
    r = requests.delete(url+"api/delete/"+pasteId)
    print(r.json()['delete'])


def SearchPaste(keyword):
    print("ID                                   Name  ")
    for i in keyword:
        res = requests.get(url+'api/search/'+i)
        pasteList = res.json()
        for paste in pasteList[i]:
            print(paste['Id']+"     "+paste['Name'])


def ShowAllPastes():
    res = requests.get(url+'api/selectDb')
    pasteList = res.json()
    print("ID                                   Name  ")
    for paste in pasteList['pastes']:
        print(paste['Id']+"     "+paste['Name'])


if __name__ == '__main__':
    parser.add_argument("action", nargs='?',
                        help="\
                Action: [get, new, search, createDb, delete, showAll,update]")
    parser.add_argument("--pasteId", default="1",
                        help="sets the pasteId for operation", required=False)
    parser.add_argument("--port", help="server port", default="8000")
    parser.add_argument("--ip", help="server ip", default="127.0.0.1")
    parser.add_argument("--keyword", help="Keyword for searching",
                        type=str, required=False)
    parser.add_argument("--name", help="PasteName", type=str,
                        required=False)
    parser.add_argument("--content", help="PasteContent", type=str,
                        required=False)
    parser.add_argument("--append",required=False)

    arg = parser.parse_args()

    url = url.format(arg.ip, arg.port)

    if arg.action == 'showAll':
        ShowAllPastes()

    if arg.action == 'search':
        if arg.keyword:
            SearchPaste(arg.keyword)
        else:
            print("please enter paste name of keyword to serch the paste")

    elif arg.action == 'get':
        if arg.pasteId:
            GetPaste(arg.pasteId)

    elif arg.action == 'delete':
        if arg.pasteId:
            DeleteAPaste(arg.pasteId)

    elif arg.action == 'update':
        print("inside update")
        if arg.pasteId!="1":
            print("there is some pasteid  "+arg.pasteId)
            UpdateAPaste(arg.pasteId,arg.content,arg.append)
        else:
            print("Please provide paste id to update")    

    if arg.action == 'new':
        if arg.name and arg.content:
            AddNewPaste(arg.name, arg.content)
        else:
            print("paste should have a name")
