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

def proposal_meat(event):
    payload = {
      "type": "carousel",
      "contents": [
        {
          "type": "bubble",
          "hero": {
            "type": "image",
            "url": "https://img.retty.me/img_repo/l/01/24513567.jpg",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
              "type": "uri",
              "label": "Line",
              "uri": "https://linecorp.com/"
            }
          },
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "魚がし食堂",
                "weight": "bold",
                "size": "xl",
                "contents": []
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "icon",
                    "url": "https://tabelog.com/ishikawa/A1701/A170101/17010307/",
                    "size": "sm"
                  },
                  {
                    "type": "icon",
                    "size": "sm"
                  },
                  {
                    "type": "icon",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                    "size": "sm"
                  },
                  {
                    "type": "icon",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                    "size": "sm"
                  },
                  {
                    "type": "icon",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "4.0",
                    "size": "sm",
                    "color": "#999999",
                    "flex": 0,
                    "margin": "md",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "margin": "lg",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Place",
                        "size": "sm",
                        "color": "#AAAAAA",
                        "flex": 1,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "石川県金沢市西念4-14-8 ",
                        "size": "sm",
                        "color": "#666666",
                        "flex": 5,
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Time",
                        "size": "sm",
                        "color": "#AAAAAA",
                        "flex": 1,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "11:00 - 23:00",
                        "size": "sm",
                        "color": "#666666",
                        "flex": 5,
                        "contents": []
                      }
                    ]
                  }
                ]
              }
            ]
          },
          "footer": {
            "type": "box",
            "layout": "vertical",
            "flex": 0,
            "spacing": "sm",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "CALL",
                  "uri": "https://tabelog.com/ishikawa/A1701/A170101/17010307/#:~:text=すべて表示する-,076-213-5428,-送る"
                },
                "height": "sm",
                "style": "link"
              },
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "WEBSITE",
                  "uri": "https://tabelog.com/ishikawa/A1701/A170101/17010307/"
                },
                "height": "sm",
                "style": "link"
              },
              {
                "type": "spacer",
                "size": "sm"
              }
            ]
          }
        },
        {
          "type": "bubble",
          "hero": {
            "type": "image",
            "url": "https://rimage.gnst.jp/rest/img/8t25vpj80000/s_0n6o.jpg?t=1594650669",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
              "type": "uri",
              "label": "Line",
              "uri": "https://linecorp.com/"
            }
          },
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "COIL",
                "weight": "bold",
                "size": "xl",
                "contents": []
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "icon",
                    "url": "https://tabelog.com/ishikawa/A1701/A170101/17010307/",
                    "size": "sm"
                  },
                  {
                    "type": "icon",
                    "size": "sm"
                  },
                  {
                    "type": "icon",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                    "size": "sm"
                  },
                  {
                    "type": "icon",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                    "size": "sm"
                  },
                  {
                    "type": "icon",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "4.0",
                    "size": "sm",
                    "color": "#999999",
                    "flex": 0,
                    "margin": "md",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "margin": "lg",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Place",
                        "size": "sm",
                        "color": "#AAAAAA",
                        "flex": 1,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "石川県金沢市袋町1-1 かなざわはこまち2F",
                        "size": "sm",
                        "color": "#666666",
                        "flex": 5,
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Time",
                        "size": "sm",
                        "color": "#AAAAAA",
                        "flex": 1,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "11:00 - 22:00",
                        "size": "sm",
                        "color": "#666666",
                        "flex": 5,
                        "contents": []
                      }
                    ]
                  }
                ]
              }
            ]
          },
          "footer": {
            "type": "box",
            "layout": "vertical",
            "flex": 0,
            "spacing": "sm",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "CALL",
                  "uri": "https://tabelog.com/ishikawa/A1701/A170101/17010307/#:~:text=すべて表示する-,076-213-5428,-送る"
                },
                "height": "sm",
                "style": "link"
              },
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "WEBSITE",
                  "uri": "https://coil-japan.jp/"
                },
                "height": "sm",
                "style": "link"
              },
              {
                "type": "spacer",
                "size": "sm"
              }
            ]
          }
        },
        {
          "type": "bubble",
          "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "See more",
                  "uri": "https://linecorp.com"
                },
                "flex": 1,
                "gravity": "center"
              }
            ]
          }
        }
      ]
    }
    container_obj = FlexSendMessage.new_from_json_dict(payload)
    line_bot_api.push_message(main.UserID, messages=container_obj)
    Text = event.message.text
    return Text
