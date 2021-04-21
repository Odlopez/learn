# https://stepik.org/lesson/24465/step/6?unit=6772
#
# Вам дана в архиве (/media/attachments/lesson/24465/main.zip) файловая структура,
# состоящая из директорий и файлов.
#
# Вам необходимо распаковать этот архив,
# и затем найти в данной в файловой структуре все директории,
# в которых есть хотя бы один файл с расширением ".py".
#
# Ответом на данную задачу будет являться файл со списком таких директорий,
# отсортированных в лексикографическом порядке.
#
# Для лучшего понимания формата задачи, ознакомьтесь с примером.
# Пример архива (/media/attachments/lesson/24465/sample.zip)
# Пример ответа (/media/attachments/lesson/24465/sample_ans.txt)

import os

res = ''
with open('text.txt', 'w') as t:
    for curDir, dirs, files in os.walk('main'):
        if len(list(filter(lambda x: x.endswith('.py'), files))):
            t.write(curDir + '\n')
