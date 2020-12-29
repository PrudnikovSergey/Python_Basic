"""
Lesson 5. Task 7.

Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
"""
import os
import json

my_f = os.path.join(os.path.dirname(__file__), 'data5_7.txt')

result = []

firms_dict = {}
tmp_dict = {}

with open(my_f, 'r', encoding="UTF-8") as file:
    for line in file:
        tmp_dict[line.split()[0]] = line.split()[1:]

profit_summary = 0
profit_count = 0

for key, value in tmp_dict.items():
    firms_dict[key] = 0
    # for itm in value:
    profit_firm = int(value[1]) - int(value[2])
    firms_dict[key] = profit_firm
    if profit_firm > 0:
        profit_summary += profit_firm
        profit_count += 1

average_dict = {"Average profit": profit_summary / profit_count}
# average_dict["Average profit"] = profit_summary / profit_count
result.append(firms_dict)
result.append(average_dict)
print(result)

with open("result5_7.json", 'w', encoding="UTF-8") as write_f:
    json.dump(result, write_f)
