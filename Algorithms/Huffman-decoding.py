# https://stepik.org/lesson/13239/step/6?after_pass_reset=true&auth=login&unit=3425

# Восстановите строку по её коду и беспрефиксному коду символов. 
# В первой строке входного файла заданы два целых числа k и l через пробел — количество различных букв, 
# встречающихся в строке, и размер получившейся закодированной строки, соответственно. 
# В следующих kk строках записаны коды букв в формате "letter: code". 
# Ни один код не является префиксом другого. 
# Буквы могут быть перечислены в любом порядке. 
# В качестве букв могут встречаться лишь строчные буквы латинского алфавита; 
# каждая из этих букв встречается в строке хотя бы один раз. 
# Наконец, в последней строке записана закодированная строка. 
# Исходная строка и коды всех букв непусты. 
# Заданный код таков, что закодированная строка имеет минимальный возможный размер.


# В первой строке выходного файла выведите строку s. 
# Она должна состоять из строчных букв латинского алфавита.
# Гарантируется, что длина правильного ответа не превосходит 10^4 символов.

# Sample Input 1:
# 1 1
# a: 0
# 0

# Sample Output 1:
# a

# Sample Input 2:
# 4 14
# a: 0
# b: 10
# c: 110
# d: 111
# 01001100100111

# Sample Output 2:
# abacabad

# Решение через отсотированный список (вместо словаря)
# n, f = [int(i) for i in input().split()]
# lst = []
# for i in range(n):
#     line = input().split()
#     symbol = line[0].replace(':', '')
#     lst.append([line[1], symbol])
# s = input()
# res = ''
# lst.sort()
# while len(s):
#     for x in lst:
#         if s.startswith(x[0]):
#             res += x[1]
#             s = s[len(x[0]):]
#             break
            
# print(res)

# Решение через деревья
class Node:
    def __init__(self, L=None, R=None, val=None, parent=None):
        self.R = R
        self.L = L
        self.val = val
        self.parent = parent
        
    def get(self, direction):
        if direction == '0':
            return self.L
        elif direction == '1':
            return self.R
        
        return None
    
    def set_child(self, direction, child):
        if direction == '0':
            self.L = child
        elif direction == '1':
            self.R = child
            
def form_tree(root, dict):
    cur_root = root
    
    for key in dict:
        for i, char in enumerate(dict[key]):
            next_root = cur_root.get(char)

            if not next_root:
                next_root = Node(parent=cur_root)
                cur_root.set_child(char, next_root)
            if i == len(dict[key]) - 1:
                next_root.val = key
                cur_root = root
            else:
                cur_root = next_root
                
def decode(s, root):
    cur_root = root
    res = ''
    while s:
        r = ''
        for char in s:
            r += char
            cur_root = cur_root.get(char)
          
            if cur_root.val:
                res += cur_root.val
                cur_root = root
                s = s[len(r):]
                
    return res
        
root = Node()

n, f = [int(i) for i in input().split()]
dict = {}
for i in range(n):
    line = input().split()
    symbol = line[0].replace(':', '')
    dict[symbol] = line[1]
s = input()

form_tree(root, dict)
res = decode(s, root)

print(res)