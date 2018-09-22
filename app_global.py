from flask import Flask
from os.path import expanduser
home = expanduser("~")

# init flask app
app     = Flask(__name__)

config = {
    "DB_FILE": home+'/.local-paste/localPaste.db'
}