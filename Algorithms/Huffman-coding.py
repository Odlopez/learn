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

s = input()
dict = {}
res = ''
for i in s:
    if dict.get(i):
        dict[i] += 1
    else:
        dict[i] = 1
lst = sorted(map(list, dict.items()), key=lambda x: (int(x[1]), x[0]))
res_lst = []

def find_index(el):
  for i, x in enumerate(lst):
    if x[1] >= el[1]:
      return i
  return len(lst)
  
if len(dict.keys()) == 1:
  for key in dict:
    dict[key] = '0'
else:
  while len(lst) > 1:
    a, b = [0, 1] if len(lst[0][0]) <= len(lst[1][0]) else [1, 0]
    res_lst.append([lst[b][0], '1'])
    res_lst.append([lst[a][0], '0'])
    
    sl = [lst[a][0] + lst[b][0], lst[a][1] + lst[b][1]]
    lst = lst[2:]
    index = find_index(sl)
    lst.insert(index, sl)

  for key in dict:
    r = ''
    for x in range(len(res_lst) - 1, -1, -1):
      if key in res_lst[x][0]:
        r += res_lst[x][1]
    dict[key] = r
  
for l in s:
  res += dict[l]


print(len(dict.keys()), len(res), sep=' ')
for k in dict:
  print(f"{k}: {dict[k]}")
  
print(res)
