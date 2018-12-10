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
       print(pasteName,pasteContent)
       pasteDetails={'name':pasteName,'content':pasteContent}
       print(pasteDetails)
       #print(clipboard.paste())
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
    print(pasteId)

def SearchAPasteById(pasteID):
    print(pasteId)   

def SearchAPasteByName(pasteName):
    print(pasteName)               

if __name__ == '__main__':
	
    parser.add_argument("action", nargs='?',
                        help="\
                        Action: [select, insert, search, createDb, delete]")
    parser.add_argument("--pasteId", default="1",
                        help="sets the pasteId for operation", required=False)
    #parser.add_argument("--keyword", help="Keyword for searching", type=str, required=False)
    parser.add_argument("--pname", help="PasteName", type=str, required=False, nargs='+')
    parser.add_argument("--pcontent", help="PasteContent", type=str, required=False,nargs='+')
    #parser.add_argument("--fileName", help="PasteFilename", type=str, required=False)
    #parser.add_argument("--limit", help="Limit on select query", required=False,
    #                    type=int, default=0)
    arg = parser.parse_args()

    if arg.pasteId:
        if arg.action == 'select':
            print("here")
            #GetPaste(pasteId=arg.pasteId)
            GetPaste(arg.pasteId)
            #AddNewPaste("here","this is new paste")
    if arg.action=='insert':
        AddNewPaste(' '.join(arg.pname),' '.join(arg.pcontent))#(arg.pname,arg.pcontent)# ' '.join(args.string)