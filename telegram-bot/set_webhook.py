import requests
from decouple import config

token = config('TELE_TOKEN')
api_url = f'https://api.telegram.org/bot{token}'
flask_url = f'https://kwon0136.pythonanywhere.com/{token}'
set_url = f'{api_url}/setWebhook?url={flask_url}'

response = requests.get(set_url)
print(response.text) # 잘 수행되는지 확인용