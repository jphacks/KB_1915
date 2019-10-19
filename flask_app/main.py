from flask import request, redirect, render_template,jsonify, flash, abort
from flask_app import app, config
from flask_app.api import main, koubun
from flask_app.line_bot_handler import bot

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

line_bot_api = LineBotApi(config.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(config.LINE_CHANNEL_SECRET)

@app.route('/')
def show_index():
  return render_template('index.html')

@app.route('/tomowarkar')
def tomowarkar():
  return config.URL
  
@app.route('/api')
def api():
  return main.text

@app.route('/callback', methods=['POST'])
def callback():
  app.logger.info(request)
  


@app.route('/koubun', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    response = koubun.koubun_main(text_input)

    return jsonify(response)