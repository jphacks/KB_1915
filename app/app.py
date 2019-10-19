from flask import Flask, request, abort, render_template

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

ACCESS_TOKEN = "3wvxOe6kSmGyu5ALt4Eh8m21CBckgjZAYZowdBXktmiKYPkkI2+7gW9JvZmVxhgi/TeF+guTEC4cSoRSYrJdS/bt+mvhasjRU4jV9A2IS3MxHet07uroE6cd2NNNvOQH8aUeU8a8zOF7LUjUhT28JQdB04t89/1O/w1cDnyilFU="
CHANNEL_SECRET = "94e56df0d31f206fd6fd62d03467e9e0"

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route('/')
def index_get():
    return render_template('index.html')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
