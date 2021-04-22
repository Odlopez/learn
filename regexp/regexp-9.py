# https://stepik.org/lesson/24470/step/15?unit=6776
#
# Вам дана последовательность строк.
# В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
# Буквой считается символ из группы \w.
# Sample Input:
#
# attraction
# buzzzz
#
# Sample Output:
#
# atraction
# buz

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'(\w)\1+', r'\1', line))
