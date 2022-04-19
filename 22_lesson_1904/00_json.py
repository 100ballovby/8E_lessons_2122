import json


with open('numbers.json') as file:
    data = json.loads(file.read())
    # трансформация строки в объект
    print(data[0])  # 2


