from flask import Flask
from requests import get

app = Flask(__name__)


#get rid of this soon
@app.route('/')
def main_page():
    return "Blah"#query



