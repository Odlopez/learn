# Создадим класс итератора, который будет выдавать случайные числа
# до указанного предела
from random import randint


class RandomIterator:
    def __init__(self, k):
        self.limit = k
        self.i = 0

    def __next__(self):
        if self.i < self.limit:
            self.i += 1
            return randint(0, 100)
        else:
            raise StopIteration

    def __iter__(self):
        return self


# Также мы можем сделать его с помощью оператора yeild:
class RandomIterator2:
    def __init__(self, k):
        self.limit = k

    def __iter__(self):
        for i in range(self.limit):
            yield randint(0, 100)


r = RandomIterator2(5)

for u in r:
    print(u)


