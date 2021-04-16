# Недавно мы считали для каждого слова количество его вхождений в строку.\
# Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит 
# самое частое слово в этом тексте
# и через пробел то, сколько раз оно встретилось. 
# Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

# В качестве ответа укажите вывод программы, а не саму программу.

# Слова, написанные в разных регистрах, считаются одинаковыми.

# Вывод в нашем случае:
# p 5

res = {}
res_arr = []
count_arr = []

with open('dataset_3363_3.txt', 'r') as text:
  for row in text:
    for word in row.strip().lower().split():
      if res.get(word):
        res[word] += 1
      else:
        res[word] = 1

for it in res:
  res_arr.append([res[it], it]) 
  count_arr.append(res[it])

max_count = max(count_arr)

res_arr = [x[1] for x in res_arr if x[0] == max_count]

print(min(res_arr), max_count)

# Второй вариант решения. Более дурацкий, зато с lambda

res = {}
arr = []

with open('dataset_3363_3.txt') as text:
  for row in text:
    for word in row.strip().lower().split():
      if res.get(word):
        res[word] += 1
      else:
        res[word] = 1

for it in res.items():
  arr.append([i for i in it])

arr = sorted(arr, key=lambda x: int(x[1]))
max = arr[len(arr) - 1][1]

arr = sorted(list(filter(lambda x: x[1] == max, arr)), key=lambda x: x[0])

print(*arr[0])