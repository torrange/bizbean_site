from flask import Flask
from requests import get
from flask import render_template

app = Flask(__name__)


#get rid of this soon
@app.route('/')
def main_page():
    return render_template('index.html')



