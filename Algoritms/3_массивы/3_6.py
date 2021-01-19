# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

size = 20
arr = [random.randint(0, 100) for _ in range(size)]
print(arr)

max_numb = 0
min_numb = 0
for i in range(size):
    if arr[i] < arr[min_numb]:
        min_numb = i
    elif arr[i] > arr[max_numb]:
        max_numb = i

if min_numb > max_numb:
    min_numb, max_numb = max_numb, min_numb
summ = 0

for i in range(min_numb + 1, max_numb):
    summ += arr[i]
print(f'минимальный элемент - {arr[min_numb]} и макс элемент - {arr[max_numb]}, сумма между - {summ}')