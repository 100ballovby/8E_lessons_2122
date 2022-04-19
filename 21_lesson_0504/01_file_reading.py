with open('pi_digits.txt') as file:  # открыть файл и присвоить его к переменной file
    pi_string = ''
    for line in file:  # прочитать каждую строку из файла
        pi_string += line.strip()  # добавить каждую строку из файла
    # метод strip() удаляет пробелы по краям строки
    print(f'π = {pi_string}', type(pi_string))

    pi_string = float(pi_string)  # преобразовать строку в десятичную дробь
    print(f'π = {pi_string}', type(pi_string))  # теперь это float, но количество знаков уменьшилось из-за ограничений python

# file.read()  <- ошибка, потому что with закрывает файл после обработки
"""Все действия с файлами с использованием конструкции with 
необходимо писать с отступом"""



