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

UserID = "U2beb3645d43471171df9ef7886968c39"

def proposal_meat(event):
    message_template = TemplateSendMessage(
        alt_text="にゃーん",
        template=ButtonsTemplate(
            text="どこに表示されるかな？",
            title="タイトルですよ",
            image_size="cover",
            thumbnail_image_url="https://任意の画像URL.jpg",
            actions=[
                URIAction(
                    uri="https://任意のページURL",
                    label="URIアクションのLABEL"
                )
            ]
        )
    )
    return message_template
    #    json_dict = json.loads(payload)
#    container_obj = FlexSendMessage.new_from_json_dict(payload)
    #line_bot_api.push_message(UserID, messages=container_obj0)
#    line_bot_api.push_message(UserID, messages=json_dict)
#    Text = event.message.text
  #  return Text
