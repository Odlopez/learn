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
