from flask import Flask

app = Flask(__name__)


#get rid of this soon
@app.route('/')
def main_page():
    return "Blah"#query



