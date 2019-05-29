from flask import Flask, render_template, request
import random
import requests
app = Flask(__name__)

@app.route('/send')
def send():
    return render_template('send.html')

@app.route('/receive')
def receive():
    # 주소를 통해 받아온 정보를 dictionary 형태로 request.args에 담는다(sky, hi 입력)
    # user: 'sky', message: 'hi'
    user = request.args.get('user') # --> 'sky'
    message = request.args.get('message') # --> 'hi'
    return render_template('receive.html', user=user, message=message)

@app.route('/choice')
def choice():
    return render_template('choice.html')

@app.route('/go')
def go():
    list = ['가자!', '가지ㅁㅏ..']
    user = request.args.get('user')
    for i in random.sample(list, 1):
        return render_template('go.html', user=user, go=i)


@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')


# 로또 번호 확인 사이트 만들기
@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'

    response = requests.get(url)
    lotto = response.json() # --> dict로 반환
#    winner = []
#    for n in range(1, 7):
#        winner.append(lotto[f'drwtNo{n}'])

    # list comprehension
    a = [lotto[f'drwtNo{n}'] for n in range(1, 7)]
   # a = [n*2 for n in range(1, 7)] # --> [2,4,6,8,10,12]
    b = lotto['bnusNo']

    winner = f'{a} + {b}'

    # my_numbers 가져오기(request.args.get('my_numbers'))
    # 문자 --> 숫자([int(n)] for n in ~)
    my_numbers = [int(n) for n in request.args.get('my_numbers').split()] # --> default: 띄어쓰기

    # 같은 숫자 갯수 찾기
    # set(): 집합 / 두개의 집합 비교 용이 / {}
    # set(a): list a 를 set으로
    # 두 집합의 교집합 구하기: &
    matched = len(set(a) & set(my_numbers)) # --> 교집합의 갯수

    # 같은 숫자의 갯수에 따른 등수
    if matched == 6:
        result = '1등입니다!'
    elif matched == 5:
        if lotto['bnusNo'] in my_numbers:
            result = '2등입니다'
        else:
            result = '3등입니다'
    elif matched == 4:
        result = '4등입니다'
    elif matched == 3:
        result = '5등입니다'
    else:
        result = '꽝입니다'

    return render_template('lotto_result.html', lotto=winner, lotto_round=lotto_round, my_numbers=my_numbers, result=result)




if __name__ == '__main__':
    app.run(debug=True)
