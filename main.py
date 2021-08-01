#-*- cording: utf-8 -*-
import psycopg2
from flask import Flask, render_template, g, request, abort
import json
import os
#import function
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

def proposal_meat():
    message_template = TemplateSendMessage(
        alt_text="うおがし食堂",
        template=ButtonsTemplate(
            text="石川県金沢市西念4-14-8",
            title="うおがし食堂",
            image_size="cover",
            thumbnail_image_url="https://img.retty.me/img_repo/l/01/24513567.jpg",
            actions=[
                URIAction(
                    uri="https://tabelog.com/ishikawa/A1701/A170101/17010307/",
                    label="ホームページ"
                )
            ]
        )
    )
    return message_template

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
    global status
    if (status == "挨拶"):
        if (message == "飲食店"):
            status = "ジャンル"
            line_bot_api.reply_message(event.reply_token,
                [
                    TextSendMessage(text='探しているジャンルを選んでください。\n「肉系」\n「魚系」\n「郷土料理系」')
                ]
            )
        elif(message == "オシャレな建物"):
            print("hoge")
        elif(message == "歴史のある建物"):
            print("fuga")
        else:
            print("ここに来てるからだめだよ")
    elif(status == "ジャンル"):
        if(message == "魚系"):
             messages = proposal_meat()
             line_bot_api.reply_message(event.reply_token,
                     [
                        messages,
                        TextSendMessage(text='この店なんてどうですか？')
                     ]
            )
#            f = ("./carousel_box/proposal_fish_uogashi.json")
            #f = ("./carousel_box/greet.json")
            #fo = open(f, "r",encoding="utf-8")
            #fl = json.load(fo)
#            text_messages = FlexSendMessage(alt_text="hoge", contents=text_message)
#            line_bot_api.push_message(function.UserID, messages=text_messages)
            #line_bot_api.push_message(function.UserID,
                    #[
                     #   FlexSendMessage(alt_text='状態を選んでね',contents = fl)
                    #]
            #)
            #fo.close()
  #                      FlexSendMessage(alt_text='最初はぐー', contents=text_message)
   #             )
            #shop = function.proposal_meat(event)
        else:
            print(message)
    else:
        print("ここに来てるからだめだよ")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
