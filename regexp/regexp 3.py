import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'\bz.{3}z\b', line):
        print(line)