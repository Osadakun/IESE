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
    line_bot_api.reply_message(event.reply_token,
            [
                FlexSendMessage(alt_text='test',contents = fl)
            ]
    )
    Text = event.message.text
    fo.close()
    return Text
