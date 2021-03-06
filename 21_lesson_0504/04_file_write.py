"""
Режимы работы с файлами:
r - read - чтение файла
w - write - запись в файл
a - append - добавление записи в файл
"""
# если файл отсутствует, он будет автоматически создан
with open('test.txt', 'w') as file:
    text = input('Введите текст: ')
    # запись в файл осуществляется функцией write(n)
    file.write(text + '\n')  # записать строку из переменной text
# литерал \n создает новую строку в файле

with open('test.txt', 'a') as file:
    text = input('Введите текст: ')
    file.write(text + '\n')  # записать строку из переменной text
