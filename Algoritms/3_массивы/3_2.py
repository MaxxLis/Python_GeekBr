# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например,
# если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
# (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.
a = [8, 3, 15, 6, 4, 2, 12, 36, 6, 5, 3]
b = []
for i, elem in enumerate(a):
    if elem % 2 == 0:
        b.append(i)
print(b)

# Генератор вместо ручного ввода:
import random

size = 10
arr = [random.randint(-100, 100) for _ in range(size)]
print(arr)