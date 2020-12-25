"""
Lesson 4. Task 5.

Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce

my_list = [itm for itm in range(100, 1001) if itm % 2 == 0]

def multiply(x, y):
    return x * y

result = reduce(multiply, my_list)
print(result)
