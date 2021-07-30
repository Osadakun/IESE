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
            "text": "金沢へようこそ！！",
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
            "text": "どんな観光名所を探していますか？",
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
            "label": "美味しいものが食べたい",
            "text": "フード"
            }
        },
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "インスタ映えする空間へ行きたい",
            "text": "インスタ"
            }
        },
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "歴史を感じたい",
            "text": "歴史"
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

    container_obj = FlexSendMessage.new_from_json_dict(payload)
    line_bot_api.push_message(main.UserID, messages=container_obj)
    Text = event.message.text
    return Text

