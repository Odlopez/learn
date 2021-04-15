# Напишите программу, которая считывает из файла строку, соответствующую тексту, 
# сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.

# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

import re
res = ''

with open('dataset_3363_2.txt', 'r') as text:
  r = text.readline().strip()
  rxd = r'\d+'
  rxD = r'\D{1}'
  letters = [a for a in re.split(rxd, r) if a != '']
  numbers = [int(a) for a in re.split(rxD, r) if a != '']

  for i in range(len(letters)):
    res += letters[i] * numbers[i]

with open('dataset_3363_2.txt', 'w') as text:
  text.write(res + '\n')
  