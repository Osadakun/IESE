#-*- cording: utf-8 -*-
import psycopg2
from flask import Flask, render_template, g, request, abort
import os
import function
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

@app.route("/")
def hello_world():
    return "HelloWorld!"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
@handler.add(MessageEvent, message=TextMessage)
def response_message(event):
    Text = event.message.text
    message = function.greet_message(event)
    print("-----------------------------------")
    print(message)
    print("-----------------------------------")
    if (message == "フード"):
        message = function.eat_type(event)
        print("-----------------------------------")
        print(message)
        print("-----------------------------------")
    elif(Text == "インスタ"):
        f = ("./carousel_box/carousel_tourism.json")
        fo = open(f,"r",encoding="utf-8")
        fl = json.load(fo)
        line_bot_api.reply_message(event.reply_token,
            [
                FlexSendMessage(alt_text='状態を選んでね',contents = fl)
            ]
        )
        fo.close()
    elif(Text == "歴史"):
        f = ("./carousel_box/carousel_history.json")
        fo = open(f,"r",encoding="utf-8")
        fl = json.load(fo)
        line_bot_api.reply_message(event.reply_token,
            [
                FlexSendMessage(alt_text='状態を選んでね',contents = fl)
            ]
        )
        fo.close()
    else:
        print("-------------------ここにきてるよ--------------------")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
