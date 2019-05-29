from flask import Flask, render_template
from random import sample
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/mulcam')
def mulcam():
    return 'This is multicampus!'

@app.route('/greeting/<string:name>')
def greeting(name): # path variable과 parameter 일치 시켜야 한다
    return f'반갑습니다, {name}님'

@app.route('/cube/<int:num>')
def cube(num):
    result = num ** 3
    return str(result) # 문자로 변환해주어야한다(현재 result는 int type)

# 주소창 주소로부터 사람수를 입력받아 점심메뉴 추천(점심메뉴 7개중 사람수만큼(ex.3) 추천)
@app.route('/lunch/<int:num>')
def lunch(num):
    menu = ['분식', '한식', '중식', '양식', '일식']
    return str(sample(menu, num))

# html을 이용하여 markup형태로 나타내기
@app.route('/html')
def html():
    # 여러줄의 문자열 표현 --> 큰따옴표 3개
    multiple_string = """
        <h1>Thin is h1 tag</h1>
        <p>This is p tag<p>  
    """
    return multiple_string

# html을 사용하기위해 templates라는 폴더를 만들고 실행할 html파일을 생성한다
# render_template: templates folder에서 html_file.html을 찾아 실행한다
@app.route('/html_file')
def html_file():
    return render_template('html_file.html')

# hi.html에서 your_name을 이용할 수 있다
@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html', your_name=name)

@app.route('/menu_list')
def menu_list():
    menu = ['분식', '한식', '중식', '양식', '일식']
    return render_template('menu_list.html', menu_list=menu)





if __name__ == '__main__':
    app.run(debug=True)