# https://stepik.org/lesson/24465/step/4?unit=6772
#
# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.
#
# Пример входного файла:
# ab
# c
# dde
# ff
#
# Пример выходного файла:
# ff
# dde
# c
# ab

with open('dataset_24465_4.txt') as text:
    reversRows = text.read().splitlines()
    reversRows.reverse()


with open('text-reverse.txt', 'w') as rev:
    rev.write('\n'.join(reversRows))
