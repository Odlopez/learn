# https://stepik.org/lesson/13238/step/9?after_pass_reset=true&auth=login&thread=solutions&unit=3424

# По данным nn отрезкам необходимо найти множество точек минимального размера, 
# для которого каждый из отрезков содержит хотя бы одну из точек.

# В первой строке дано число 1 ≤ n ≤ 100 отрезков. 
# Каждая из последующих nn строк содержит по два числа 0 ≤ l ≤ r ≤ 1, задающих начало и конец отрезка. 
# Выведите оптимальное число mm точек и сами mm точек. 
# Если таких множеств точек несколько, выведите любое из них.

# Sample Input 1:
# 3
# 1 3
# 2 5
# 3 6

# Sample Output 1:
# 1
# 3 

# Sample Input 2:
# 4
# 4 7
# 1 3
# 2 5
# 5 6

# Sample Output 2:
# 2
# 3 6 

n = int(input())
lst = [[int(i) for i in input().split()] for x in range(n)]
lst = sorted(lst, key=lambda x: x[1])
res = [lst[0][1]]

for i in range(1, len(lst)):
    if lst[i][0] <= res[-1]:
        continue
    res.append(lst[i][1])
    
print(len(res))
print(*res)