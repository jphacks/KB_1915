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
  app.logger.info("line_bot_api: " + str(line_bot_api))
  app.logger.info("handler: " + str(handler))
  # get X-Line-Signature header value
  signature = request.headers['X-Line-Signature']
  app.logger.info("signature: " + str(signature))
  # get request body as text
  body = request.get_data(as_text=True)
  app.logger.info("Request body: " + str(body))

  # handle webhook body
  try:
      handler.handle(body, signature)
  except InvalidSignatureError:
      abort(400)

  return 'OK'
  
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

@app.route('/koubun', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    response = koubun.koubun_main(text_input)

    return jsonify(response)