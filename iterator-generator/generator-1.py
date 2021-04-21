# Создадим простейший генератор
def foo(limit):
    i = 0
    while i < limit:
        yield i
        i += 4


z = foo(25)

for k in z:
    print(k)
