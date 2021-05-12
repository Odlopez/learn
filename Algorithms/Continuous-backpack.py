# https://stepik.org/lesson/13238/step/10?after_pass_reset=true&auth=login&unit=3424

# Первая строка содержит количество предметов 1 ≤ n ≤ 10^3 и вместимость рюкзака 0 ≤ W ≤ 2⋅10^6. 
# Каждая из следующих nn строк задаёт стоимость 0 ≤ c_i ≤ 2⋅10^6 
# и объём 0 ≤ w_i ≤ 2⋅10^6 предмета (n, W, c_i, w_i — целые числа). 
# Выведите максимальную стоимость частей предметов 
# (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), 
# помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
# Sample Input:
# 3 50
# 60 20
# 100 50
# 120 30

# Sample Output:
# 180.000

n, W = [int(i) for i in input().split()]
lst = sorted([[int(i) for i in input().split()] for x in range(n)], key=lambda x: x[0]/x[1])
res = 0

while W and len(lst):
    if lst[-1][1] <= W:
        res += lst[-1][0]
        W -= lst[-1][1]
        lst.pop()
    else:
        cost = lst[-1][0] / lst[-1][1]
        res += cost * W
        W = 0
        
print(f'{res:.3f}')