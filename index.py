from flask import Flask 
from flask import request
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
PORT=8081

@app.route("/test")
def test():
    response = requests.get('http://test1:8081/check')
    return response.text


@app.route("/hello")
def hello_world():
    name = request.args.get('name',default="")
    if name == "":
        return "Hello, world!"
    else:
        return "Hello, "+ name +"!"


@app.route("/hello", methods=['POST'])
def hello_post():
    return "This method is unsupported.", 405

@app.route("/check")
def check():
    return "All is well!"



@app.route("/check", methods=['POST'])
def check_post():
    return "This method is unsupported.", 405

if __name__ == "__main__":
    app.run(port = 8081, host = "0.0.0.0")