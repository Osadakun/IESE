#-*- cording: utf-8 -*-
from flask import Flask, render_template, g, request, abort
import os
import main
import psycopg2
import json
from linebot.models import *

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

app = Flask(__name__)
line_bot_api = LineBotApi(os.environ["ACCESS_TOKEN"])
handler = WebhookHandler(os.environ["CHANNEL_SECRET"])

def greet_message(event):
    payload = {
    "type": "bubble",
    "direction": "ltr",
    "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "$B6bBt$X$h$&$3$=!*!*(B",
            "align": "center",
            "contents": []
        }
        ]
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "$B$I$s$J4Q8wL>=j$rC5$7$F$$$^$9$+!)(B",
            "align": "center",
            "contents": []
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "$BH~L#$7$$$b$N$,?)$Y$?$$(B",
            "text": "$B%U!<%I(B"
            }
        },
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "$B%$%s%9%?1G$($9$k6u4V$X9T$-$?$$(B",
            "text": "$B%$%s%9%?(B"
            }
        },
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "$BNr;K$r46$8$?$$(B",
            "text": "$BNr;K(B"
            }
        }
        ]
    }
    }

    container_obj = FlexSendMessage.new_from_json_dict(payload)
    line_bot_api.push_message(main.UserID, messages=container_obj)
    Text = event.message.text
    return Text

def eat_type(event):
    payload = {
    "type": "bubble",
    "direction": "ltr",
    "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "$B$I$s$J$b$N$,?)$Y$?$$$G$9$+!)(B",
            "align": "center",
            "contents": []
        }
        ]
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "$B%8%c%s%k$rA*$s$G$M(B",
            "align": "center",
            "contents": []
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "$BFy7O(B",
            "text": "$BFy(B"
            }
        },
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "$B5{7O(B",
            "text": "$B5{(B"
            }
        },
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "$B6?EZNAM}7O(B",
            "text": "$B6?EZNAM}(B"
            }
        }
        ]
    }
    }

    container_obj = FlexSendMessage.new_from_json_dict(payload)
    line_bot_api.push_message(main.UserID, messages=container_obj)
    Text = event.message.text
    return Text

