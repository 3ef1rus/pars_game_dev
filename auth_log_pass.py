import json
import requests

headers = {
    'accept': '*/*',
    'accept-language': 'ru',
    'content-type': 'application/json',
    'origin': 'https://attend.gdcevents.gdconf.com',
    'referer': 'https://attend.gdcevents.gdconf.com/login/ru-RU/login',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-called-from-server': 'false',
}

json_data = {
    'emailAddress': 'michael@28software.com',
    'password': '1234Adimptzu',
    'shouldReturnRefreshToken': True,
}

response = requests.post('https://attend.gdcevents.gdconf.com/auth/api/login',
                         headers=headers, json=json_data)
json_data = json.dumps(response.json(), indent=2)

# Запись JSON-данных в файл
dictionary = eval(json_data)
auth_key = "Bearer "+dictionary['accessToken']
