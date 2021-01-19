# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

size = 20
arr = [random.randint(0, 10) for _ in range(size)]
print(arr)

min_1, min_2 = 100, 100
for i in arr:
    if min_1 > i:
        min_1 = i
    elif min_2 > i:
        min_2 = i
print(min_1, min_2)