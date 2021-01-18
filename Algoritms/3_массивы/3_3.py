# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

size = 10
arr = [random.randint(0, 100) for _ in range(size)]
print(arr)

# max_elem = 0
# max_numb = 0
# min_elem = 100
# min_numb = 0
# for i, elem in enumerate(arr):
#     if max_elem < elem:
#         max_elem = elem
#         max_numb = i
#     if min_elem > i:
#         min_elem = elem
#         min_numb = i
#
# arr[min_numb], arr[max_numb] = arr[max_numb], arr[min_numb]
#
# print(arr)

# второй вариант - короче и меньше переменных
max_numb = 0
min_numb = 0
for i in range(size):
    if arr[i] < arr[min_numb]:
        min_numb = i
    elif arr[i] > arr[max_numb]:
        max_numb = i
arr[min_numb], arr[max_numb] = arr[max_numb], arr[min_numb]
print(arr)