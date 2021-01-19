# 4. Определить, какое число в массиве встречается чаще всего.
import random

size = 100
arr = [random.randint(0, 20) for _ in range(size)]
print(arr)
replay = {}
max_number = 0
max_ch = 0
for i in set(arr):
    replay[i] = 0
    for j in arr:
        if i == j:
            replay[i] += 1
    if max_number < replay[i]:
        max_number = replay[i]
        max_ch = i
print(replay)
print(max_ch, max_number)

# 2 вариант - проще - НО Я ЭТО НЕ ПОНИМАЮ ...
diction = {}
for item in arr:
    if item in diction.keys():
        diction[item] += 1
    else:
        diction[item] = 1
print(diction)

