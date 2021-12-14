""" Функция range() - генератор математических последовательностей
range(x) -> 0...x - 1  (х не входит в последовательность)
range(y, x) -> y...x - 1
range(y, x, step) -> y...x-1, c шагом step
"""
for i in range(10):  # 0, 1, 2, 3....9
    print(i, end=', ')

print()

for j in range(40, 50):  # 40, 41, 42, 43....49
    print(j, end=', ')

print()

for k in range(1, 11, 2):  # 1, 3....9
    print(k, end=', ')
