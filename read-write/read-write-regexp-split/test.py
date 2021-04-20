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

# Второй вариант, почти такой же, как и первый:

# words = []
# nums = []

# with open('dataset_3363_2.txt') as text:
#   row = text.readline().strip()
#   words = [i for i in re.split(r'\d+', row) if i]
#   nums = [int(i) for i in re.split(r'\D+', row) if i]

# with open('dataset_3363_2.txt', 'w') as text:
#   for i, it in  enumerate(words):
#      text.write(it * nums[i])

# Наш вывод должен быть:
# wwwwwwwwwwwwwwwppppppppppppppppppppIvvvvvvvvvvvvvOOOOOOOOOOOwwwwwwwwwwwwwrrrrrrrrrrUUUUUUUUUUUUUUUUUUUvvvvvvvvvvvvvvvvSSSSSSSSSSSSSSEEEeettttttttttttttttttkkkkkkkkkAAMMMMMMMMMMMMMMMMMzzzzzzzzzzuuuuuuuuuuuuuuuuuussssssssssssssVVVVVVVVVVVVVwwwwwwwwwwwwwwBBBBBBBBBBvvvvvvvvvvLLLLLLLLLLLLLRRRRRRRRRRRRRRRTTxxxxxxxxxxoooooooooooohhhhhhhhhhhhhhhhhhhhrwwwwwwwwwwwwwwwwHHHHHHdddddddddddddddcccSOOOOOOOOOOOO
