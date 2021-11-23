nums = [56, 12, 778, 81, 9, 5, 23, 2, 0, 3]

print(nums[1])  # 12
""" Перебор через индексы 
Перебор - это просмотр каждого элемента списка по отдельности 
1. Цикл for 
2. Функция len(), которая измеряет длину списка 
"""
for index in range( len(nums) ):  # 0...<длина списка>
    print(f'№{index}, Элемент: {nums[index]};')

"""Перебор через значения"""
for element in nums:
    if element % 2 == 0:  # проверяю, делится ли элемент на 2 без остатка
        print(f'Элемент: {element};')

