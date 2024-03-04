from python.etc.flaskTemplate import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/checkOk',methods=['GET'])
def getCheckOk():
    return "Ok"

@app.route('/test', methods=['POST'])
def test():
    # แสดงข้อมูลที่ได้รับจาก webhook
    data = request.json
    print(data)

    # ตอบกลับไปยังผู้ส่ง
    return jsonify({'status': 'success', 'data': data}), 200


@app.route('/webhook', methods=['POST'])
def webhook():
    # แสดงข้อมูลที่ได้รับจาก webhook
    data = request.json
    print(data)

    # ตอบกลับไปยังผู้ส่ง
    return jsonify({'status': 'success', 'data': data}), 200

if __name__ == '__main__':
    ip='188.166.191.51'
    app.run(debug=True,host=ip, port=5000,ssl_context=('path/to/cert.pem', 'path/to/key.pem'))
