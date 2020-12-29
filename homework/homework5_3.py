"""
Lesson 5. Task 3.

Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

my_f = open("data5_3.txt", 'r', encoding='UTF-8')
n = 0
personal_less_20k = ''
salary_sum = 0

for line in my_f:
    n += 1
    tmp = line.split()
    salary_sum += int(tmp[1])
    if int(tmp[1]) < 20000:
        personal_less_20k += tmp[0] + ", "

print('Сотрудники с окладом менее 20 000: ' + personal_less_20k)
average_salary = salary_sum / n
print(f'Средний оклад работников - {average_salary}')
my_f.close()