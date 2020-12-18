"""
Lesson 3. Task 1.

Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
def my_div():
    try:
        dividend = int(input('Введите число (делимое)\n>'))
        divider = int(input('Введите число (делитель)\n>'))
    except ValueError:
        return 'Ошибка ввода, вы не ввели число'

    try:
        result = dividend / divider
        return result
    except ArithmeticError:
        return 'Делить на 0 нельзя'

print(my_div())


