"""
Lesson 5. Task 6.

Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import os

my_f = os.path.join(os.path.dirname(__file__), 'data5_6.txt')
tmp_dict = {}


with open(my_f, 'r', encoding="UTF-8") as file:
    for line in file:
        tmp = line.split(':')
        tmp_dict[tmp[0]] = tmp[1].split()

result_dict = {}
for key, value in tmp_dict.items():
    result_dict[key] = 0
    for itm in value:
        try:
            result_dict[key] += int(itm.split('(')[0])
        except ValueError:
            continue

print(result_dict)