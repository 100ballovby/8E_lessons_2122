years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]

print(f'Изначальный вид: {years}. Индекс 3: {years[3]}')
years.insert(3, 'меня вставили')
print(f'Измененный вид: {years}. Индекс 3: {years[3]}')
