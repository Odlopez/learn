import requests

r = requests.post('https://echo.htmlacademy.ru', data={'test': "ОК"})

rr = requests.get('http://example.com')

param = {"date": "14-04-2021", "login": "shmyaka", "rain": "nope"}
rx = requests.get('http://example.com', params=param)

url = 'http://bla-bla-bla.com'
cookies = {'taram': 'param'}

rc = requests.get(url, cookies=cookies)

# print(r.encoding)
print(rc.text)
print(rx.url)
# print(rr.json())
# print(rr.text)
# print(rr.content)