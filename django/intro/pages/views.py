from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html')

def hola(request):
    return render(request, 'hola.html')

def dinner(request):
    menu = ['팟타이', '분짜', '얌운센', '쌀국수']
    pick = random.choice(menu)
    #return render(request, 'dinner.html', {'pick':pick}) # 변수 넘기기{함수에서 사용한 변수 ,dinner.html에서 사용할 변수명}
    context = {'pick':pick}  # official
    return render(request, 'dinner.html', context=context)

def hello(request, name):
    context = {'name':name}
    return render(request, 'hello.html', context)

def introduce(request, name, age):
    context = {'name':name, 'age':age}
    return render(request, 'introduce.html', context)


# variable routing을 통해 숫자 2개를 받아 곱셉 결과 출력
def times(request, num1, num2):
    result = num1 * num2
    context = {'num1':num1, 'num2':num2, 'result':result}
    return render(request, 'times.html', context)

# 반지름을 인자로 받아 원의 넓이 구하기
def circle(request, radius):
    area = radius*radius*3.14 # == (radius**2)*3.14
    context = {'radius':radius, 'area':area}
    return render(request, 'circle.html', context)

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
    return render(request, 'template_language.html', context)

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
    return render(request, 'birth.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    # name=message에 담겨 GET 형태로 던져진 요청을 받아와 message 변수에 담는다
    # .get(): 딕셔너리 자료형의 value값 리턴하는 방식
    # --> request.GET에서 키값이 'message'인 value값을 불러와라
    name = request.GET.get('name')
    message = request.GET.get('message')
    context = {'name':name, 'message':message}
    return render(request, 'catch.html', context)

# 로또번호 추천번호 출력(lotto/get)
def lotto(request):
    return render(request, 'lotto.html')

def get(request):
    name = request.GET.get('name')
    num = request.GET.get('num')
    numbers = range(1, 46)

    choice = []
    for i in num:
        choice.append(sorted(random.sample(numbers, 6)))

    context = {'choice':choice, 'name':name, 'num':num}
    return render(request, 'get.html', context)