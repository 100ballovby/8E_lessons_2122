import random as r
import string

n = int(input('Введите количество символов пароля: '))

symb = string.printable
password = ''
for i in range(n):
    password += symb[r.randint(0, len(symb) - 1)]

print(password)