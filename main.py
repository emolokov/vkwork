import time
import requests, os
from datetime import datetime
from alive_progress import alive_bar

# вызываем переменные окружения
TOKEN_USER = "6408db196408db196408db19b167101b0f664086408db1902789c09a971b1d1d680ddd4"
VERSION = 5.199
DOMAIN = "omsksluhi"


# через api vk вызываем статистику постов
# response = requests.get('https://api.vk.com/method/wall.get',
# params={'access_token': TOKEN_USER,
#         'v': VERSION,
#         'domain': DOMAIN,
#         'count': 10,
#         'filter': 'all'})


def chekValidGroup():
    if not os.path.isfile("group.txt"):
        print("Файл не существует")
        return

    if os.path.getsize("group.txt") == 0:
        print('Файл пустой')
        return

    current_datetime = datetime.now()
    folder_name = 'valid'
    file_name = f'{current_datetime.strftime("%Y-%m-%d_%H-%M-%S")}.txt'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, "w") as f:
        pass
    lines = []
    with open("group.txt", 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    with alive_bar(len(lines)) as bar:
        # count = 0
        for l in lines:
            # if (count != 0):
            #     if count % 50 ==0:
            #      time.sleep(30)
            try:
                response = requests.get('https://api.vk.com/method/wall.get',
                                        params={'access_token': TOKEN_USER,
                                                'v': VERSION,
                                                'domain': l,
                                                'count': 1,
                                                'filter': 'all'})
            except:
                continue

            if 'error' in response.json():
                print(response.json())
                continue
            try:
                data = response.json()['response']['items'][0]['date']
            except:
                continue
            current_timestamp = int(time.time())
            three_days_ago = current_timestamp - 3 * 24 * 60 * 60
            if data < three_days_ago:
                with open(file_path, "a") as f:
                    f.write(f'{l}\n')
                print(l)
            bar()
            # count+=1
            time.sleep(0.1)

    if os.path.getsize(file_path) == 0:
        os.remove(file_path)


def parseGroup():
    if not os.path.isfile("valid/in.txt"):
        print("Файл не существует")
        return

    lines = []
    with open("in.txt", 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    with alive_bar(len(lines)) as bar:
        # count = 0
        for l in lines:

            try:
                response = requests.get('https://api.vk.com/method/wall.get',
                                        params={'access_token': TOKEN_USER,
                                                'v': VERSION,
                                                'domain': l,
                                                'count': 20,
                                                'filter': 'all'})
            except:
                continue

            if 'error' in response.json():
                print(response.json())
                continue
            try:
                data = response.json()['response']['items'][0]['date']
            except:
                continue
            current_timestamp = int(time.time())
            three_days_ago = current_timestamp - 3 * 24 * 60 * 60
            if data < three_days_ago:
                with open(file_path, "a") as f:
                    f.write(f'{l}\n')
                print(l)
            bar()
            # count+=1
            time.sleep(0.1)


if __name__ == "__main__":
    parseGroup()
