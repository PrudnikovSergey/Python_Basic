"""
Lesson 5. Task 2.

Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_f = open("data5_2.txt", 'r', encoding='UTF-8')
n = 0

for line in my_f:
    n += 1
    words_count = len(line.split())
    print(f'{n}-я строка файла: {line}')
    print(f'Количество слов в строке - {words_count} \n')

print(f'Общее колчество строк в файле - {n}')
my_f.close()
