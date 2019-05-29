def hello(func):
    print('hi hi')
    func() # --> bye()를 실행한 것과 동일
    print('hi hi')


@hello
def bye():
    print('bye bye')

bye()