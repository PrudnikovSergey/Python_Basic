"""
Lesson 3. Task 3.

Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def my_func(x: int, y: int, z: int) -> int:
    """
    Возвращает сумму двух наибольших из трёх заданных аргументов
    :param x: int
    :param y: int
    :param z: int
    :return: int
    """
    excess = min(x, y, z)
    return sum([x, y, z]) - excess

print(my_func(12, 6, 4))
print(my_func(12, 7, 8))
print(my_func(1, 5, 4))