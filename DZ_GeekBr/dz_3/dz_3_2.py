# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

dict_data = {
    'name': 'Ivan',
    'last_name': 'Ivanov',
    'year': '1976',
    'city': 'Moscow',
    'e_mail': 'ivan@mail.ru',
    'phone': '+7-917-687-4513'
}


def data(**kwargs):
    print('\n'.join("{}: {}".format(a, b) for a, b in kwargs.items()))  # реализация печати одной строкой,
    # если только не имелось ввиду, что именно данные о челе должны быть в одной строке

    return kwargs


data(name=dict_data['name'], last_name=dict_data['last_name'], year=dict_data['year'], city=dict_data['city'],
           e_mail=dict_data['e_mail'], phone=dict_data['phone'])


