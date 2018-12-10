import argparse
import requests

parser = argparse.ArgumentParser()

url="http://0.0.0.0:8000/"
def GetPaste(pasteId):
    r = requests.get(url+"api/get/"+pasteId)    
    print(r.text)

def ShowAllPastes():
    r = requests.get(url)    
    print(r)
    

if __name__ == '__main__':
	
    parser.add_argument("action", nargs='?',
                        help="\
                        Action: [select, insert, search, createDb, delete]")
    parser.add_argument("--pasteId", default="1",
                        help="sets the pasteId for operation", required=False)
    #parser.add_argument("--keyword", help="Keyword for searching", type=str, required=False)
    #parser.add_argument("--name", help="PasteName", type=str, required=False)
    #parser.add_argument("--content", help="PasteContent", type=str, required=False)
    #parser.add_argument("--fileName", help="PasteFilename", type=str, required=False)
    #parser.add_argument("--limit", help="Limit on select query", required=False,
    #                    type=int, default=0)
    arg = parser.parse_args()

    if arg.action == 'select':
        if arg.pasteId:
            GetPaste(pasteId=arg.pasteId)
        else:
            ShowAllPastes()

	#GetPaste()