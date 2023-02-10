from flask import Flask
app = Flask(__name__)
#dd
@app.route('/')
def hello_world():
    return 'Hello, Docker!'