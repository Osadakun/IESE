#-*- cording: utf-8 -*-
import psycopg2
from flask import Flask, render_template, g, request, abort
import os
import json
from linebot.models import *

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]

app = Flask(__name__)
line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

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
    UserID = event.source.user_id
    Text = event.message.text
    f = ("./carousel_box/greet.json")
    fo = open(f,"r",encoding="utf-8")
    fl = json.load(fo)
    line_bot_api.reply_message(event.reply_token,
            [
                FlexSendMessage(alt_text='',contents = fl)
            ]
    )
    fo.close()
    
if __name__ == "__main__":
     port = int(os.getenv("PORT", 5000))
     app.run(host="0.0.0.0", port=port)
