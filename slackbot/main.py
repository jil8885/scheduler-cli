from pathlib import Path
import sqlite3, sys
from . import __version__
from slacker import Slacker
import os
import time
import websocket
import json
from .input_command import handler

key = os.getenv('slack')
def slack_server():
    slack = Slacker(key)
    if slack.rtm.connect():
        response=slack.rtm.start()
        sock_endpoint=response.body['url']
        slack_socket=websocket.create_connection(sock_endpoint)

        while True:
            msg = json.loads(slack_socket.recv())
            try:
                string = handler(msg['text'], msg['user'])
                slack.chat.post_message(channel=msg['user'], text=string)
            except:
                pass

    else:
        print("connect fail")