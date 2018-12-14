import argparse
import requests
import uuid
import json
#import clipboard

parser = argparse.ArgumentParser()
debug = 0
url="http://0.0.0.0:5000/"
#def GetPaste(pasteId):
def GetPaste(pasteId):
    
    print(pasteId)
    r = requests.get(url+"api/get/"+pasteId)   
    print(r.text)

def AddNewPaste(pasteName,pasteContent):
    try:       
       pasteDetails={'name':pasteName,'content':pasteContent}
       r=requests.put(url+"api/new",json=pasteDetails)
       print(r.status_code)
       if r.status_code == 200:
           print(r.content)
       else:
           print("error") 

    except Exception as e:
       if debug:
           print(e, e.message) 

def UpdateAPaste(pasteId,pasteContent):
    print(pasteId,pasteContent)

def DeleteAPaste(pasteId):
    try:
        print("inside try")
        r=requests.delete(url+"api/delete/"+pasteId)
        print(r.status_code)
    except Exception as e:
        if debug:
            print(e, e.message)   

def SearchAPasteByName(pasteName):
    for i in pasteName:
        res = requests.get(url+'api/search/'+i)
        print(res.text)
    """pasteList=GetAllPastes()
    print("pname", pasteName)
    for paste in pasteList:
        #print(paste)
        for i in paste:
            #print(str(i["Name"].encode('utf-8')))

            if pasteName[0] in  i["Name"] or pasteName[0] in i['Content']:
                print(i['Id'])
                for pasteDetail in paste:
            if pasteName in pasteDetail:#str(pasteDetail['Name']).contains(pasteName):
                print("ID  "+pasteDetail['Id']+"; Name  "+pasteDetail['Name'])"""

    print(pasteName)               

def SearchAPasteByKeyword(keyword):
    pasteList=GetAllPastes()
    for paste in pasteList:
        for pasteDetail in paste:
            #print(type(str(pasteDetail['Name'])))
            if str(pasteDetail['Name']).contains(keyword) and str(pasteDetail['content']).contains(keyword):
                print("ID  "+pasteDetail['Id']+"; Name  "+pasteDetail['Name'])

    print(keyword)

def GetAllPastes():
    r=requests.get(url+'api/selectDb')
    pastesJson=json.loads(r.text)
    return pastesJson.values()

def ShowAllPastes():
    pasteList=GetAllPastes()
    for paste in pasteList:
        for pasteDetail in paste:
            print("ID  "+pasteDetail['Id']+"; Name  "+pasteDetail['Name'])
        

if __name__ == '__main__':
	
    parser.add_argument("action", nargs='?',
                        help="\
                        Action: [select, insert, search, createDb, delete,showAll]")
    parser.add_argument("--pasteId", default="1",
                        help="sets the pasteId for operation", required=False)
    parser.add_argument("--keyword", help="Keyword for searching", type=str, required=False)
    parser.add_argument("--pname", help="PasteName", type=str, required=False, nargs='+')
    parser.add_argument("--pcontent", help="PasteContent", type=str, required=False,nargs='+')
    #parser.add_argument("--fileName", help="PasteFilename", type=str, required=False)
    #parser.add_argument("--limit", help="Limit on select query", required=False,
    #                    type=int, default=0)
    arg = parser.parse_args()

    if arg.action=='showAll':
        ShowAllPastes()

    if arg.action=='search':
        if arg.pname:
            print("following pastes contain the pastename you entered please run \"python lpcli.py select --pasteId \" alongwith the pasteId in front of the paste\n")
            SearchAPasteByName(arg.pname)

        elif arg.keyword:
            print("following pastes contain the keyword you entered please run \"python lpcli.py select --pasteId \" alongwith the pasteId in front of the paste\n")
            SearchAPasteByKeyword(arg.keyword)    
        else:
            print("please enter paste name of keyword to serch the paste")      
    if arg.pasteId:
        if arg.action == 'select':
            GetPaste(arg.pasteId)
        if arg.action=='delete':
            DeleteAPaste(arg.pasteId)    
           
    if arg.action=='insert':
        if arg.pname:
            AddNewPaste(' '.join(arg.pname),' '.join(arg.pcontent))
        else:
            print("paste should have a name")