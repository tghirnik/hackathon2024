import os
import ai
import flask
import webex

service = flask.Flask(__name__)

@service.route("/webhook", methods = ["POST"])
def webhook():
    data = flask.request.json["data"]
    webex.message(data[webex.PID], ai.ans(data[webex.TEXT]))
    return flask.jsonify({ "status": "received" })

def run():
    print("service running...")
    service.run(int(os.getenv("PORT") or "5000"))