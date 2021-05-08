import flask
import wolframalpha
from flask import Flask, request


app = Flask(__name__)
app.secret_key = "secretkey"


@app.route("/")
def index():
    return "API OPERATIONAL"


@app.route("/operation", methods=["POST"])
def function():
    content = flask.request.json
    print(content)
    data = content['query']
    app_id = 'UUH8YU-436RYJUGUA'
    client = wolframalpha.Client(app_id)
    result = client.query(data)
    try:
        answer = next(result.results).text
    except:
        answer = "This is an invalid query"
    return answer


