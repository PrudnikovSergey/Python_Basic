"""
Lesson 3. Task 4.

Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""


def my_mov(x: float, y: int) ->float :
    """
    Вовзращает возведение параметра X в отрицательную Y-степень
    :param x: float
    :param y: int
    :return: float
    """
    result = 1
    for i in range(abs(y)):
        result *= 1/x
    return result if y < 0 else 1 / result

print(my_mov(2.0, -1))
print(my_mov(2.0, -2))
print(my_mov(2.0, -3))
