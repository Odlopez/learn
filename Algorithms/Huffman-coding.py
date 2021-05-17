# https://stepik.org/lesson/13239/step/5?after_pass_reset=true&auth=login&unit=3425

# По данной непустой строке s длины не более 10^4, 
# состоящей из строчных букв латинского алфавита, # постройте оптимальный беспрефиксный код.
# В первой строке выведите количество различных букв k, встречающихся в строке, 
# и размер получившейся закодированной строки. 
# В следующих k строках запишите коды букв в формате "letter: code". 
# В последней строке выведите закодированную строку.

# Sample Input 1:
# a

# Sample Output 1:
# 1 1
# a: 0
# 0

# Sample Input 2:
# abacabad

# Sample Output 2:
# 4 14
# a: 0
# b: 10
# c: 110
# d: 111
# 01001100100111


from collections import defaultdict
# Получили строку
s = input()
# Создали словарь для хранения данных и смволах и их количестве повторений
# defaultdict используем для того, чтобы новый ключ сразу шел со значением 0
dict = defaultdict(int)
# Переменная для итоговой зашифрованной строки
res = ''
# Заполнили словарь всеми встречающимися в строке символами
for i in s:
    dict[i] += 1
# Создаём список из пар "сивол-количество повторений"
# и сортируем по количеству повторений от меньшего к большему
lst = sorted(map(list, dict.items()), key=lambda x: (int(x[1]), x[0]))
# Создали пустой список, в который будем складывать результаты наших "шагов"
# по алгоритму Хаффмана (символ или группа символов и 1 или 0, присвоенные им)
res_lst = []

# Функция для поиска индекса элемента в нашем списке
# "вес" которого больше или равен переданному в качестве аргумента
def find_index(el):
  for i, x in enumerate(lst):
    if x[1] >= el[1]:
      return i
  return len(lst)

# Если в строке был только один символ, обрабатываем этот случай отдельно  
if len(dict.keys()) == 1:
  for key in dict:
    dict[key] = '0'
# В противном случае:
else:
  # Пока в нашем списке пар "символ-количество повторений" больше одного элемента
  while len(lst) > 1:
    # Берем два самых редко встречающихся символа
    a, b = [0, 1] if len(lst[0][0]) <= len(lst[1][0]) else [1, 0]
    # Считаем, что первый из двух элементов имеет "меньший вес" (то есть количество повторений),
    # даже, если это количество повторений равно. Поэтому определяем его в левую сторону дерева Хаффмана.
    # То есть присваиваем элементу 0, а другому - присваиваем 1
    res_lst.append([lst[a][0], '0'])
    res_lst.append([lst[b][0], '1'])
    # "Сливаем" два наших элемента в один
    sl = [lst[a][0] + lst[b][0], lst[a][1] + lst[b][1]]
    # Обрезаем список на два элемента с начала (выбрасываем те, которые мы только что использовали)
    # И добавляем наш новый, "спаянный" элемент в список перед другим элементом,
    # вес которого больше, или равен
    lst = lst[2:]
    index = find_index(sl)
    lst.insert(index, sl)

  # Проходим по нашему словарю с символами из исходной строки
  for key in dict:
    # Заводим переменную, для накапливания результирующего двоичного кода для символа
    r = ''
    # Во вложенном цикле, проходим для каждого символа по сформированному
    # списку "шагов Хаффмана" и ищем совпадения символа. То есть, если искомый символ "х"
    # а в списке шагов Хаффмана находим элемент ["saxv", "1"], значит в результирующий код добавляем "1"
    for x in range(len(res_lst) - 1, -1, -1):
      if key in res_lst[x][0]:
        r += res_lst[x][1]
    # Заменяем в нашем словаре для искомого символа количество повторений в строке на 
    # результирующий двоичный код для этого символа
    dict[key] = r

# Проходим по строке и заменяем все символы в ней, на двоичный код  
for l in s:
  res += dict[l]

# Печатаем сколько у нас получилось всего символов, и длину строки
print(len(dict.keys()), len(res), sep=' ')
# Печатаем для каждого символа двоичный код, соответствующий ему 
for k in dict:
  print(f"{k}: {dict[k]}")
# Печатаем зашифрованную строку
print(res)
