# https://stepik.org/lesson/24470/step/14?unit=6776
#
# Вам дана последовательность строк.
# В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
# Буквой считается символ из группы \w.
# Sample Input:
#
# this is a text
# "this' !is. ?n1ce,

# Sample Output:
#
# htis si a etxt
# "htis' !si. ?1nce,
import sys
import re


def ter(m):
    return m.group(2) + m.group(1) + m.group(3)


for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'\b(\w)(\w)(\w*)\b', ter, line))

# Также есть второй вариант решения, делает то же самое, но интересный синтаксис

# for line in sys.stdin:
#     line = line.strip()
#     line = re.sub(r"\b(\w)(\w)(\w*)\b", r"\2\1\3", line)
#     print(line)