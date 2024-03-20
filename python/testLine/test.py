from flask import Flask, request, abort

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

line_bot_api = LineBotApi('Ct11jM+O7Xvv1PKjXvcTxm+361ZF4nacQpE+M7k7P+tEZ7mEZAlShPwESbTEfuwD7o/NbVCNYTbpS1JWZiGEMmocmW/0yIV1XytI/z2jKeWNJnEnpmGBiBLeuo6Hn9xUpSjOdwblied4nDe0ff6/nAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('20fdc9ed291ea83e62def31a0b1d7f93')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['x-line-signature']

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