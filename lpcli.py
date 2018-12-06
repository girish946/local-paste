import argparse
import requests

parser = argparse.ArgumentParser()

url="http://0.0.0.0:8000/"
def GetPaste(pasteId):
    #parser.add_argument("-a","--action_to_take", required=True,help="Name of command")
    #parser.add_argument("-u","--uuid",help="uuid of post")
    #args = parser.parse_args()
    r = requests.get(url+"api/get/"+pasteId)
    #data=r.json()
    print(r.text)
    #parser.add_argument("-n","--uname",help="name of paste")
    #parser.add_argument("-c","--content",help="content of paste")

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

    if arg.pasteId:
        if arg.action == 'select':
            GetPaste(pasteId=arg.pasteId)
	#GetPaste()