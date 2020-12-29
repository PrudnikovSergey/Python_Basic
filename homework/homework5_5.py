"""
Lesson 5. Task 5.

Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

numbers_to = [random.randint(1, 99) for x in range(random.randint(10, 15))]
print(f'Исходный сгенерированный набор чисел: {numbers_to}')
sum_numbers_start = sum(numbers_to)
print(f'Сумма набора чисел: {sum_numbers_start}')

with open("result5_5.txt", 'w', encoding="UTF-8") as file:
    file_content = ' '.join(map(str, numbers_to))
    file.write(file_content)

with open("result5_5.txt", 'r', encoding="UTF-8") as file:
    numbers = map(int, file.read().split())

sum_result = sum(numbers)
print(f'Для проверки - сумма из записанных в файл чисел: {sum_result}')
