import json
import csv

table_file = 'prices.csv'  # название таблицы


with open('series_GOLD.json') as jf:
    data = json.loads(jf.read())
    gas = data['data']['rates']
    with open(table_file, 'w', newline='') as table:  # открыть таблицу и не добавлять пустые строки между строк
        writer = csv.writer(table)  # записывает данные в таблицу
        headers = ['Date', 'Price', 'Unit', '$50', '$100', '$150']  # заголовки таблицы
        writer.writerow(headers)  # записываю заголовки таблицы в таблицу
        for unit in gas:
            row = []  # пустая строка таблицы
            try:
                row.append(unit)
                row.append(gas[unit]['XAU'] * 28.34)
                row.append('гр')  # перевести единицы измерения в метры кубические
                # добавил в список данные из json-файла
                writer.writerow(row)  # записываю строчку в таблицу
            except KeyError:
                pass  # пропустить выполнение


