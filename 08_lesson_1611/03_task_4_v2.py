n = input('Введите число: ')
mult = 1

for integer in n:
    print(f'{mult} * {integer} = {mult * int(integer)}')
    mult *= int(integer)

print(mult)

