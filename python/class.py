class Person:  # Person이라는 class 선언
    name = '사람의 고유한 속성'
    age = '출생 이후부터 삶을 마감할 때까지의 기간'

    def greeting(self):  # class 안의 함수 --> method
        print(f'{self.name}이 인사합니다. 안녕하세요!')

    def eating(self):
        print(f'{self.name}은 밥을 먹고 있습니다.')

    def aging(self):
        print(f'{self.name}은 현재 {self.age}살이고, 현재 나이를 먹어가는 중입니다...')

sky = Person()  # Person이라는 class로부터 sky라는 인스턴스 하나를 만든다
print(sky.name)
print(sky.age)

sky.name = 'sky'
sky.age = 28

print(sky.name)
print(sky.age)

sky.greeting()
sky.eating()
sky.aging()