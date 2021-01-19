# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

import random
summ = 0

# list_input = list(i for i in input().split())
# print(list_input)

# Генератор матрицы:
# matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(4)]
# for line in matrix:
#     for item in line:
#         print(f'{item:>4}', end='')
#     print()

# мой вариант

matrix_hand = [[], [], [], []]
for i in range(4):
    matrix_hand[i] = [int(input()) for _ in range(4)]
    summ = 0
    for el in matrix_hand[i]:
        summ += el
    matrix_hand[i].append(summ)

for line in matrix_hand:
    for item in line:
        print(f'{item:>4}', end='')
    print()

# вариант преподавателя
M = 5
N = 4
matrix = []

for i in range(N):
    row = []
    summ = 0

    for j in range(M - 1):
        num = int(input(f'строка {i}, элемент {j}: '))
        summ += num
        row.append(num)

    row.append(summ)
    matrix.append(row)


for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print()