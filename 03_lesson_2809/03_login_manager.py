login = input('Введите логин: ')  # данные, которые вводит пользователь
password = input('Введите пароль: ')  # данные, которые вводит пользователь

correct_password = '12345qwerty'  # правильные данные
correct_login = 'GreatRaksin'  # правильные данные

if (login == correct_login) and (password == correct_password):
    # если ввод пользователя совпадает с правильными данными, я его пускаю "на сайт"
    print('Добро пожаловать!')
else:  # иначе не пускаю
    print('Логин и/или пароль неправильные!')


