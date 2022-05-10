"""
Методы проверки символов строки:
.isupper() - проверяет, является ли символ большой буквой
.islower() - проверяет, является ли символ маленькой буквой
"""
string = 'Hello! There is my first string!'
lower_symbols = 0
for symbol in string:
    if symbol.islower():
        lower_symbols += 1

print(lower_symbols, 'маленьких букв.')
