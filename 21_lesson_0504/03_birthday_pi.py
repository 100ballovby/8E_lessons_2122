with open('pi_million_digits.txt') as file:
    pi = ''
    for line in file:
        pi += line.strip()

    birthday = input('Введите дату рождения в формате ДДММГГ: ')
    if birthday in pi:  # если последовательность даты рождения есть среди символов числа π
        print('Ваша дата рождения есть в числе π!')
    else:
        print('Вашей даты рождения в числе π нет!')