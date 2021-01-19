# 9. Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

count = int(input('введите кол-во вводимых чисел: '))
max_chr = 0
for i in range(count):
    sum_chr = 0
    chr_input = input('введите следующее число: ')
    for j in chr_input:
        sum_chr += int(j)
    if max_chr < sum_chr:
        max_chr = sum_chr
        max_input = chr_input
print(f'{max_input} введено, сумма его чисел {max_chr}')