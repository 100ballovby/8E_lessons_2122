import string

n = input('Введите число: ')
mult = 1
restricted = string.punctuation  # здесь все спецсимволы !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

for integer in n:
    if integer not in restricted:  # если цифра числа не спецсимвол
        print(f'{mult} * {integer} = {mult * int(integer)}')
        mult *= int(integer)


print(mult)

