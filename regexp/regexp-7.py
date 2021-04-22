# https://stepik.org/lesson/24470/step/13?unit=6776
#
# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова, состоящего только из латинских
# букв "a" (регистр не важен), на слово "argh".
#
# Примечание:
# Обратите внимание на параметр count у функции sub.
#
# Sample Input:
#
# There’ll be no more "Aaaaaaaaaaaaaaa"
# AaAaAaA AaAaAaA
#
# Sample Output:
#
# There’ll be no more "argh"
# argh AaAaAaA
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'\ba+\b', 'argh', line, 1, re.IGNORECASE))