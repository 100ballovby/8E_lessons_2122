"""Проверка числа на делимость. Число вводится пользователем"""

number = int(input('Введи число: '))

# % - это остаток от деления
if (number % 5 == 0) and (number % 3 == 0):  # делимость и на 3, и на 5
    print('Число делится на 5 и на 3!')
else:
    print('Число НЕ делится на 5 или на 3!')