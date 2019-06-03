import requests
import random
from decouple import config

token = config('TELE_TOKEN')
api_url = f'https://api.telegram.org/bot{token}'
# 본인 telegram 계정 id
chat_id = config('CHAT_ID')
# input()을 통해 사용자로부터 입력 받아 메세지 전송
#text = input('메세지를 입력하세요: ')
# 로또 번호 추천 메세지
text = random.sample(range(1, 46), 6)

# python으로 caht message 보내기
response = requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')