# возведение в степень без **
def power(num, p):
    """
    Функция возводит число num в степень p
    :param num: int число
    :param p: int степень
    :return: num ^ p
    """
    res = 1
    for i in range(p):  # повторить p раз
        res *= num
    return res


for number in range(1, 16):
    print(f'{number} ^ 2 = {power(number, 2)}')
