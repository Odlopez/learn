# Вам дано описание наследования классов в следующем формате.
# <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
# Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

# Или эквивалентно записи:

# class Class1(Class2, Class3 ... ClassK):
#     pass
# Класс A является прямым предком класса B, если B отнаследован от A:


# class B(A):
#     pass


# Класс A является предком класса B, если
# A = B;
# A - прямой предок B
# существует такой класс C, что C - прямой предок B и A - предок C

# Например:
# class B(A):
#     pass

# class C(B):
#     pass

# # A -- предок С


# Вам необходимо отвечать на запросы, является ли один класс предком другого класса

# Важное примечание:
# Создавать классы не требуется.
# Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов.

# В следующих n строках содержится описание наследования классов. 
# В i-й строке указано от каких классов наследуется i-й класс. 
# Обратите внимание, что класс может ни от кого не наследоваться. 
# Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), 
# что класс не наследуется явно от одного класса более одного раза.

# В следующей строке содержится число q - количество запросов.

# В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
# Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

# Формат выходных данных
# Для каждого запроса выведите в отдельной строке слово "Yes", 
# если класс 1 является предком класса 2, и "No", если не является.

classes = {}

def createClass(name):
  if not classes.get(name):
    classes[name] = {
      'parents': set(),
      'children': set([name])
    }

def setChild(parent, child):
  if not classes.get(parent):
    createClass(parent)
    
  classes[parent]['children'].add(child)
  
  for par in classes[parent]['parents']:
    setChild(par, child)
    
def setClass(name, *par):
  if not classes.get(name):
    createClass(name)
    
  for x in par:
    classes[name]['parents'].add(x)
    setChild(x, name)
    
def isParent(parent, child):
  res = 0

  if not classes.get(parent) or not classes.get(child):
    return 0
  elif parent not in classes[child]['parents'] and not len(classes[child]['parents']) and parent != child:
    return 0
  elif parent in classes[child]['parents'] or parent == child:
    return 1
  else:
    for i in classes[child]['parents']:
      res += isParent(parent, i)
    return res
    
def isAnswer(parent, child):
  print('Yes' if isParent(parent, child) else 'No')

n = int(input())

for x in range(n):
    s = input().split(' : ')
    name = s[0]
    par = []
    
    if (len(s) > 1):
        par = s[1].split()
    
    setClass(name, *par)

q = int(input())

for i in range(q):
    s = input().split()
    isAnswer(*s)

# Sample Input:

# 4
# A
# B : A
# C : A
# D : B C
# 4
# A B
# B D
# C D
# D A

# Sample Output:

# Yes
# Yes
# Yes
# No