# https://stepik.org/lesson/24470/step/9?unit=6776
#
# Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
# Sample Input:
#
# zabcz
# zzz
# zzxzz
# zz
# zxz
# zzxzxxz
# Sample Output:
#
# zabcz
# zzxzz

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'\bz.{3}z\b', line):
        print(line)