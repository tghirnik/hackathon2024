import os
import ai
import json
import time
import requests

PID = "personId"
TEXT = "text"

__URI = "https://webexapis.com/v1/messages"

__ITEMS = "items"

__ROBOT = os.getenv("WEBEX_ROBOT")
__TOKEN = os.getenv("WEBEX_TOKEN")
__DELAY = int(os.getenv("DELAY_MS") or "1000")

__HEADERS = { "Authorization": f"Bearer {__TOKEN}", "Content-Type": "application/json" }

def query():
    # need to know whether does this fetch every message or simply unread
    messages = requests.get(__URI, headers = __HEADERS).json()[__ITEMS]
    return [ message for message in messages if message[PID] is not __ROBOT ]

def message(pid = "", message = ""):
    data = json.dumps({ PID: pid, TEXT: message })
    return requests.post(__URI, headers = __HEADERS, data = data).json()

def orchestrate():
    print("script running...")
    while True:
        for msg in query():
            time.sleep(__DELAY / 1000)
            message(msg[PID], ai.ans(msg[TEXT]))