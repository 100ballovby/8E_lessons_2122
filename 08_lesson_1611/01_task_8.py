# задача про ферзя
# Задача про слона
x1 = int(input('Введите х: '))
y1 = int(input('Введите y: '))
x2 = int(input('Введите х2: '))
y2 = int(input('Введите y2: '))

if abs(x1 - y1) == abs(x2 - y2) or (x1 == x2) or (y1 == y2):
    print('YES')
else:
    print('NO')


