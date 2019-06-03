from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/write')
def wrrite():
    return render_template('write.html')

@app.route('/send')
def send():
    token = '774736412:AAE4JdzhVDEX96_ZAMkFXxixyf1rST7m2S4'
    api_url = f'https://api.telegram.org/bot{token}'
    chat_id = '871858295'
    # write page로부터 받아온 message 사용
    text = request.args.get('message')

    response = requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')
    return '전송 완료' # just 확인용






if __name__ == '__main__':
    app.run(debug=True)