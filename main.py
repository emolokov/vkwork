import requests
# вызываем переменные окружения
TOKEN_USER = "6408db196408db196408db19b167101b0f664086408db1902789c09a971b1d1d680ddd4"
VERSION = 5.199
DOMAIN = "club17666171"

# через api vk вызываем статистику постов
response = requests.get('https://api.vk.com/method/wall.get',
params={'access_token': TOKEN_USER,
        'v': VERSION,
        'domain': DOMAIN,
        'count': 100,
        'filter': 'all'})
        

data = response.json()['response']['items']
for i in data:
    if 'продам' in i['text'].lower():
        print(DOMAIN+"_"+str(i['id']))
        print()
        print(i['text'])
    

