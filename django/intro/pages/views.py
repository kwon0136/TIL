from django.shortcuts import render
import random
from datetime import datetime
import json
import requests

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def hola(request):
    return render(request, 'pages/hola.html')

def dinner(request):
    menu = ['팟타이', '분짜', '얌운센', '쌀국수']
    pick = random.choice(menu)
    #return render(request, 'dinner.html', {'pick':pick}) # 변수 넘기기{함수에서 사용한 변수 ,dinner.html에서 사용할 변수명}
    context = {'pick':pick}  # official
    return render(request, 'pages/dinner.html', context=context)

def hello(request, name):
    context = {'name':name}
    return render(request, 'pages/hello.html', context)

def introduce(request, name, age):
    context = {'name':name, 'age':age}
    return render(request, 'pages/introduce.html', context)


# variable routing을 통해 숫자 2개를 받아 곱셉 결과 출력
def times(request, num1, num2):
    result = num1 * num2
    context = {'num1':num1, 'num2':num2, 'result':result}
    return render(request, 'pages/times.html', context)

# 반지름을 인자로 받아 원의 넓이 구하기
def circle(request, radius):
    area = radius*radius*3.14 # == (radius**2)*3.14
    context = {'radius':radius, 'area':area}
    return render(request, 'pages/circle.html', context)

def template_language(request):
    menus = ['분짜', '팟타이', '쌀국수', '텃만쿵']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'orange', 'cherry', 'blueberry']
    empty_list = ['justin', 'sky']
    datetimenow = datetime.now()
    context = {
        'menus':menus,
        'my_sentence':my_sentence,
        'empty_list':empty_list,
        'datetimenow':datetimenow,
        'messages':messages
    }
    return render(request, 'pages/template_language.html', context)

# 생일이 맞는지 확인하는 페이지 만들기
def birth(request):
    datetimenow = datetime.now()
    #today = datetime.today().strftime('%m-%d')
    #birth_date = '09-02'
    if datetime.now().month == 6 and datetime.now().day == 19: # python 에서 &사용X
        result = True
    else:
        result = False
    context = {'result':result}
    return render(request, 'pages/birth.html', context)

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    # name=message에 담겨 GET 형태로 던져진 요청을 받아와 message 변수에 담는다
    # .get(): 딕셔너리 자료형의 value값 리턴하는 방식
    # --> request.GET에서 키값이 'message'인 value값을 불러와라
    name = request.GET.get('name')
    message = request.GET.get('message')
    context = {'name':name, 'message':message}
    return render(request, 'pages/catch.html', context)

# 실습: 로또번호 추천번호 출력(lotto/get)
def lotto(request):
    return render(request, 'pages/lotto.html')

def get(request):
    name = request.GET.get('name')
    num = request.GET.get('num')
    numbers = range(1, 46)

    #choice = []
    for i in num:
        choice = sorted(random.sample(numbers, 6))

    context = {'choice':choice, 'name':name, 'num':num}
    return render(request, 'pages/get.html', context)

# 나눔로또 홈페이지에서 1등번호를 받아와 몇등 당참인지 확인하기
def lotto2(request):
    return render(request, 'pages/lotto2.html')

def picklotto(request):
    name = request.GET.get('name')
    res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=861')
    lotto = json.loads(res.text) # json file을 dictionary 형태로 변환(변환할 json file은 str, binary등의 형태여야함 --> .text)

    winner = []
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])

    picked = sorted(random.sample(range(1,46), 6))
    matched = len(set(winner) & set(picked)) # winner와 picked의 교집합의 개수

    if matched == 6:
        result = '1등입니다'
    elif matched == 5:
        result = '3등입니다'
    elif matched == 4:
        result = '4등입니다'
    elif matched == 3:
        result = '5등입니다'
    else:
        result = '꽝..'

    context = {'name':name, 'result':result}
    return render(request, 'pages/picklotto.html', context)

def art(request):
    return render(request, 'pages/art.html')

def result(request):
    #1. form 태그로 날린 데이터를 받는다
    word = request.GET.get('word')

    #2. artii API를 통해 보낸 응답 결과를 text로 fonts에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

    #3. fonts(str)를 font 리스트 형태로 저장한다.
    fonts = fonts.split('\n')

    #4. fonts(list)안에 들어있는 요소 중 하나를 선택하여 font에 저장한다.
    font = random.choice(fonts)

    #5. 사용자로부터 받은 word와 random하게 뽑은 font를 가지고 다시 요청을 보낸다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {'result':result}
    return render(request, 'pages/result.html', context)

#__________________________________________________________________________________________________________

# POST 방식
def user_new(request):
    return render(request, 'user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {'name':name, 'pwd':pwd}
    return render(request, 'pages/user_create.html', context)

# static file load
def static_example(request):
    return render(request, 'pages/static_example.html')