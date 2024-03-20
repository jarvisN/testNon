import requests
import json

webhook_url = "http://127.0.0.1:5000/callback"  # แทนที่ด้วย URL ของ webhook ของคุณ
channel_access_token = "Ct11jM+O7Xvv1PKjXvcTxm+361ZF4nacQpE+M7k7P+tEZ7mEZAlShPwESbTEfuwD7o/NbVCNYTbpS1JWZiGEMmocmW/0yIV1XytI/z2jKeWNJnEnpmGBiBLeuo6Hn9xUpSjOdwblied4nDe0ff6/nAdB04t89/1O/w1cDnyilFU="
fake_signature = "20fdc9ed291ea83e62def31a0b1d7f93" 

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + channel_access_token,
    "x-line-signature": fake_signature  # Add this line to include the signature
}

data = {
    "events": [
        {
            "type": "message",
            "replyToken": "00000000000000000000000000000000",
            "source": {
                "userId": "U32e95a974436b4e6c8685f691a6a939e",
                "type": "user"
            },
            "timestamp": 1462629479859,
            "message": {
                "type": "text",
                "id": "100001",
                "text": "test"
            }
        }
    ]
}

response = requests.post(webhook_url, headers=headers, data=json.dumps(data))
print(response.text)
