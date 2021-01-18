# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.
numbers = [i for i in range(2, 100)]
numbers_1 = [i for i in range(2, 10)]
multiple = {}
for i in numbers_1:
    multiple[i] = 0
    for j in numbers:
        if j % i == 0:
            multiple[i] += 1
print(multiple)

# 2 способ, без генерации последовательностей
for i in range(2, 10):
    multiple[i] = 0
    for j in range(2, 100):
        if j % i == 0:
            multiple[i] += 1
print(multiple)