# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
a = int(input('введите число 1:'))
b = int(input('введите число 2:'))
c = int(input('введите число 3:'))

if (a > b and a < c) or (a < b and a > c):
    print(f'{a} среднее')
elif (b > a and b < c) or (b < a and b > c):
    print(f'{b} среднее')
else:
    print(f'{c} среднее')

# Более простая запись:

# if (b < a < c) or (b > a > c):
#     print(f'{a} среднее')
# elif (a < b < c) or (a > b > c):
#     print(f'{b} среднее')
# else:
#     print(f'{c} среднее')
