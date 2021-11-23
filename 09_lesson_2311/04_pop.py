years = [2000, 2001, 2002, 'меня вставили', 2003, 2004, 2005, 2006]

print(f'Изначальный вид: {years}.')
years.pop()
print(f'Измененный вид: {years}.')
years.pop(3)
print(f'Измененный вид: {years}.')

