"""Проверка числа на делимость. Число вводится пользователем"""

number = int(input('Введи число: '))

# % - это остаток от деления
if (number % 5) == 0:  # если остаток от деления на 5 равен 0
    print('Число делится на 5!')
    print('Молодец!')
else:
    print('Число НЕ делится на 5!')