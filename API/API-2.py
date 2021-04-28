# https://stepik.org/lesson/24476/step/4?auth=login&unit=6781
#
# Name:	Alex
# Client Id:	354589a8900698cf069e
# Client Secret:	511542a9f7d23dfdc8d5e9194cf00f65

# В этой задаче вам необходимо воспользоваться API сайта artsy.net
#
# API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
#
# В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
#
# Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию о имени художника и годе рождения.
# Выведите имена художников в порядке неубывания года рождения.
# В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке.

# Примечание:
# В качестве имени художника используется параметр sortable_name в кодировке UTF-8.
#
# Пример входных данных:
# 4d8b92b34eb68a1b2c0003f4
# 537def3c139b21353f0006a6
# 4e2ed576477cc70001006f99
#
# Пример выходных данных:
# Abbott Mary
# Warhol Andy
# Abbas Hamra

import requests
import json

params = {
    'client_id': '354589a8900698cf069e',
    'client_secret': '511542a9f7d23dfdc8d5e9194cf00f65'
}
url = 'https://api.artsy.net/api/artists/{}'
res = {}

r = requests.post('https://api.artsy.net/api/tokens/xapp_token', params=params)

token = json.loads(r.text)['token']

headers = {
    'X-Xapp-Token': token
}

with open('dataset_24476_4.txt', encoding='UTF-8') as text:
    for row in text:
        r_get = requests.get(url.format(row.rstrip()), headers=headers)

        name = r_get.json()['sortable_name']
        birthday = r_get.json()['birthday']

        res[name] = birthday

res = sorted(res.items(), key=lambda x: (x[1], x[0]))
res = [i[0] for i in res]

print(*res, sep='\n')