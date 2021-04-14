# Ссыль на доку (быстрый старт)
# https://docs.python-requests.org/en/latest/user/quickstart/
import requests

r = requests.post('https://echo.htmlacademy.ru', data={'test': "ОК"})

rr = requests.get('https://api.github.com/events')

print(r.encoding)

# print(rr.json())
print(r.text)
print(r.content)