#-*- cording: utf-8 -*-
from flask import Flask, render_template, g, request, abort
import os
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
    f = ('./carousel_box/greet.json')
    fo = open(f,'r',encoding="utf-8")
    fl = json.load(fo)
    print("^^-----------------------------------^^")
    print(fl)
    print("^^-----------------------------------^^")
    line_bot_api.reply_message(event.reply_token,
            [
                FlexSendMessage(alt_text='test',contents = fl)
            ]
    )
    Text = event.message.text
    fo.close()
    print("^^^-----------------------------------^^^")
    print(fl)
    print("^^^-----------------------------------^^^")
    return Text

def eat_type(event):
    UserID = event.source.user_id
    payload = {
    "type": "bubble",
    "direction": "ltr",
    "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "どんなものが食べたいですか？",
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
            "text": "ジャンルを選んでね",
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
            "label": "肉系",
            "text": "肉"
            }
        },
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "魚系",
            "text": "魚"
            }
        },
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "郷土料理系",
            "text": "郷土料理"
            }
        }
        ]
    }
    }

    #f = ('./carousel_box/type.json')
    #fo = open(f,'r',encoding="utf-8")
    #fl = json.load(fo)
    container_obj = FlexSendMessage.new_from_json_dict(payload)
    line_bot_api.push_message(UserID, messages=container_obj)
#    line_bot_api.reply_message(event.reply_token,
 #           [
     #           FlexSendMessage(alt_text='test',contents = fl)
      #      ]
    #)
    print("^^-----------------------------------^^")
    #print(FlexSendMessage(alt_text='test',contents = fl))
    print("^^-----------------------------------^^")
    Text = event.message.text
    fo.close()
    return Text

