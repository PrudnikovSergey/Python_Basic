"""
Lesson 3. Task 2.

Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

def data(name: str, surname: str, year: int, city: str, email: str, phone: int):
    """
    Отображает данные о пользователе на экране в одну строку
    :param name: str
    :param surname: str
    :param year: int
    :param city: str
    :param email: str
    :param phone: int
    :return:
    """
    return f'{name} {surname}, birth year: {year}, contacts: {phone}, {email}, city - {city}'

print(data(name='Sergey', surname='Prudnikov', city='Krasnogorsk', year=1990,
           email='kanonir86rus@yandex.ru', phone=89651376898))