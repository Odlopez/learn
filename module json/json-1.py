# https://stepik.org/lesson/24473/step/4?unit=6777
#
# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов,
# которые соответствуют классам. У каждого JSON-объекта есть поле name,
# которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
#
# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
#
# Эквивалент на Python:
#
# class A:
#     pass
#
# class B(A, C):
#     pass
#
# class C(A):
#     pass
#
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно,
# и что никакой класс не наследуется явно от одного класса более одного раза.
#
# Для каждого класса вычислите предком скольких классов он является и выведите
# эту информацию в следующем формате.
#
# <имя класса> : <количество потомков>
#
# Выводить классы следует в лексикографическом порядке.
#
# Sample Input:
#
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

# Sample Output:
#
# A : 3
# B : 1
# C : 2
import json

l = """
[
    {"name": "G", "parents": ["F"]},
    {"name": "A", "parents": []},
    {"name": "B", "parents": ["A"]},
    {"name": "C", "parents": ["A"]},
    {"name": "D", "parents": ["B", "C"]},
    {"name": "E", "parents": ["D"]},
    {"name": "F", "parents": ["D"]},
    {"name": "X", "parents": []},
    {"name": "Y", "parents": ["X", "A"]},  
    {"name": "Z", "parents": ["X"]},
    {"name": "V", "parents": ["Z", "Y"]},
    {"name": "W", "parents": ["V"]}
]
"""
arr = json.loads(l)
ans_dict = {}
ans = []
for it in arr:
    for p in it["parents"]:
        for k in arr:
            if k["name"] == p:
                it["parents"].extend(k["parents"])

for it in arr:
    ans_dict[it["name"]] = len(list(filter(lambda x: x["parents"].count(it["name"]), arr))) + 1

for key, val in ans_dict.items():
    ans.append(key + " : " + str(val))

ans.sort()

print(*ans, sep="\n")
