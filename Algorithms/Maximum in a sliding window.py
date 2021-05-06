# Ссылка на задачу
# https://stepik.org/lesson/41234/step/5?unit=19818

# Вариант, который работает, но не проходит проверку на время
# x = [2, 1, 5]
# m = 1
# current = 0
#
# arr = list(sorted(x[:m]))
#
# for el in x[m: len(x)]:
#     print(arr[len(arr) - 1], end=' ')
#     arr.remove(x[current])
#     current += 1
#     max_el = next((x for x in arr if x > el), 'max')
#     index = len(arr) if max_el == 'max' else arr.index(max_el)
#     arr.insert(index, el)
# print(arr[len(arr) - 1], end=' ')

