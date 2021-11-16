import random as r
import string

n = int(input('Введите количество символов пароля: '))
symb = input('Нужны ли спец.символы? (+/-) ')
digits = input('Нужны ли цифры? (+/-)')

letters = string.ascii_letters
symbols = string.punctuation
numbers = string.digits

pre = letters
if symb == '+' and numbers == '+':
    pre += (symbols + numbers)
elif symb == '+':
    pre += symbols
elif digits == '+':
    pre += numbers

password = ''

for i in range(n):
    password += r.choice(pre)

print(password)
