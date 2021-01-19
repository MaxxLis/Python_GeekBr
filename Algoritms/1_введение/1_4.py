# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.
ch_start = input('задайте нижнюю границу диапазона символов: ')
ch_end = input('задайте верхнюю границу диапазона символов: ')

numb_start = ord(ch_start) - ord('a') + 1
numb_end = ord(ch_end) - ord('a') + 1

count_simb = ord(ch_end) - ord(ch_start) - 1

print(f'порядковый номер в алфавите {ch_start} равен {numb_start}')
print(f'порядковый номер в алфавите {ch_end} равен {numb_end}')
print(f'символов между {ch_start} и {ch_end} - {count_simb}')
