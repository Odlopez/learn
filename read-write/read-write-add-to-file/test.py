# Имеется файл с данными по успеваемости абитуриентов. 
# Он представляет из себя набор строк, где в каждой строке записана следующая информация:

# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

# Поля внутри строки разделены точкой с запятой, оценки — целые числа.

# Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его 
# среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.

# Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные значения, 
# разделённые пробелом, последней строкой в файл с ответом.

# В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной 
# строкой со средними оценками по трём предметам.

res = {1:0, 2:0, 3:0}
count = 0
res_arr = []
end_str = ''

with open('dataset_3363_4.txt', 'r') as text:
  for row in text:
    res_arr.append([])

    for i, ass in enumerate(row.strip().split(';')):
      if ass.isdigit():
        res[i] += int(ass)
        res_arr[count].append(int(ass))

    count += 1

with open('dataset_3363_4.txt', 'w') as text:
  for x in res_arr:
    text.write(str((x[0] + x[1] + x[2]) / 3) + '\n')

for x in res:
  end_str += str(res[x] / len(res_arr)) + ' '

with open('dataset_3363_4.txt', 'a') as text:
  text.write(end_str)


# Второй способ решения:

# создаем массив, в который будем накапливать полученные из файла данные
# массив очень неочевидное решение, лучше было бы словарь,
# но с массивом менее многословно
res = [0, 0, 0, 0, []]

# функция, с помощью которой мы будем наполнять наш искомый массив:
# в первый элемент - накапливаем все оценки по математике
# во второй - все оценки по физике
# в третий - все по языку
# в четвертый - считаем общее количество учеников
# в пятый элемент (подмассив) накапливаем средние оценки по каждому ученику подряд 
def foo(math, physic, lang):
  res[0] += int(math)
  res[1] += int(physic)
  res[2] += int(lang)
  res[3] += 1
  res[4].append((int(math) + int(physic) + int(lang)) / 3)

# выделяем из файла строки, а из них только числа - интересующие нас оценки
with open('dataset_3363_4.txt') as text:
  for row in text:
    s = [it for it in row.strip().split(';') if it.isdigit()]
    foo(s[0], s[1], s[2])

# теперь проходим по нашему массиву и записываем в файл оценки
with open('dataset_3363_4.txt', 'w') as text:
  for it in res[4]:
    text.write(str(it) + '\n')
  for i in range(3):
    text.write(str(res[i] / res[3]) + ' ')

# Наш вывод должен быть таким:
# 72.0
# 65.33333333333333
# 78.66666666666667
# 57.333333333333336
# 66.0
# 65.66666666666667
# 44.333333333333336
# 54.333333333333336
# 52.666666666666664
# 81.66666666666667
# 75.0
# 59.0
# 60.333333333333336
# 63.0
# 37.666666666666664
# 73.33333333333333
# 36.333333333333336
# 81.33333333333333
# 64.0
# 53.0
# 83.33333333333333
# 91.33333333333333
# 52.666666666666664
# 58.0
# 85.0
# 81.0
# 71.33333333333333
# 41.0
# 52.333333333333336
# 55.0
# 70.66666666666667
# 62.0
# 69.66666666666667
# 61.333333333333336
# 39.0
# 66.66666666666667
# 49.666666666666664
# 60.0
# 51.666666666666664
# 41.0
# 46.333333333333336
# 65.33333333333333
# 58.0
# 62.0
# 59.0
# 80.66666666666667
# 64.33333333333333
# 48.0
# 66.66666666666667
# 56.666666666666664
# 66.66666666666667
# 50.666666666666664
# 33.333333333333336
# 45.666666666666664
# 81.0
# 69.0
# 53.0
# 69.66666666666667
# 73.66666666666667
# 39.333333333333336
# 72.66666666666667
# 64.66666666666667
# 76.33333333333333
# 88.33333333333333
# 82.66666666666667
# 53.0
# 78.0
# 66.0
# 60.666666666666664
# 76.0
# 83.33333333333333
# 76.33333333333333
# 73.0
# 60.666666666666664
# 87.0
# 76.33333333333333
# 81.33333333333333
# 27.0
# 74.66666666666667
# 59.0
# 59.333333333333336
# 57.666666666666664
# 62.0
# 68.66666666666667
# 84.33333333333333
# 60.0
# 71.33333333333333
# 81.33333333333333
# 77.33333333333333
# 66.33333333333333
# 53.666666666666664
# 76.0
# 57.333333333333336
# 54.333333333333336
# 56.666666666666664
# 67.0
# 62.0
# 43.666666666666664
# 56.0
# 70.33333333333333
# 55.0
# 52.333333333333336
# 67.66666666666667
# 58.333333333333336
# 69.66666666666667
# 73.0
# 80.0
# 79.0
# 49.0
# 60.333333333333336
# 90.33333333333333
# 73.33333333333333
# 70.0
# 79.0
# 64.0
# 51.333333333333336
# 72.66666666666667
# 60.666666666666664
# 65.33333333333333
# 78.33333333333333
# 77.0
# 62.333333333333336
# 59.333333333333336
# 55.333333333333336
# 88.0
# 42.333333333333336
# 38.666666666666664
# 47.666666666666664
# 52.666666666666664
# 80.66666666666667
# 66.33333333333333
# 61.666666666666664
# 52.333333333333336
# 72.33333333333333
# 78.33333333333333
# 53.0
# 61.333333333333336
# 49.333333333333336
# 58.666666666666664
# 60.0
# 57.666666666666664
# 45.333333333333336
# 70.66666666666667
# 69.66666666666667
# 52.0
# 74.33333333333333
# 46.0
# 68.66666666666667
# 59.0
# 58.666666666666664
# 56.666666666666664
# 72.0
# 72.66666666666667
# 53.333333333333336
# 63.666666666666664
# 70.33333333333333
# 62.3525641025641 65.26282051282051 63.39102564102564 