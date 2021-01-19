# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# вариант преподавателя
# M = 5
# N = 4
# matrix = []
#
# for i in range(N):
#     row = []
#     summ = 0
#
#     for j in range(M - 1):
#         num = int(input(f'строка {i}, элемент {j}: '))
#         summ += num
#         row.append(num)
#
#     row.append(summ)
#     matrix.append(row)
#
#


matrix = [
    [1, 5, 8, 6, 5],
    [2, 6, 7, 2, 4],
    [9, 6, 7, 4, 1],
    [3, 4, 6, 7, 9],
]

for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print()

print('*' * 50)

min_column = [9 for i in range(5)]
max_el = 0
for i in matrix:
    for j in range(len(i)):
        if min_column[j] > i[j]:
            min_column[j] = i[j]

for i in min_column:
    if i > max_el:
        max_el = i

print(min_column)
print(max_el)

