#-*- cording: utf-8 -*-
import psycopg2
from flask import Flask, render_template, g, request, abort
import os
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

status = "挨拶"

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

@handler.add(FollowEvent)
def follow(event):
    line_bot_api.reply_message(event.reply_token,
        [
            TextSendMessage(text='観光名所提案Botです。\n友達追加ありがとうございます!!'),
            TextSendMessage(text='探しているものを以下から選んで送信してください。\n「飲食店」\n「オシャレな建物」\n「歴史のある建物」')
        ]
    )

@handler.add(MessageEvent, message=TextMessage)
def response_message(event):
    message = event.message.text
    if (status == "挨拶"):
        if (message == "飲食店"):
            line_bot_api.reply_message(event.reply_token,
                [
                    TextSendMessage(text='探しているジャンルを選んでください。\n「肉系」\n「魚系」\n「郷土料理系」')
                ]
            )
            status = "ジャンル"
        elif(message == "オシャレな建物"):
            print("hoge")
        elif(message == "歴史のある建物"):
            print("fuga")
        else:
            print(message)
    elif(status == "ジャンル"):
            if(message == "肉系"):
                print("成功だ")
            else:
                print(messagge)
    else:
        print(status)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
