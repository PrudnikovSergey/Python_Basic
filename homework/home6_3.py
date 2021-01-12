"""
Lesson 6. Task 3.

 Реализовать базовый класс Worker (работник), в котором определить атрибуты:
 name, surname, position (должность), income (доход).
 Последний атрибут должен быть защищенным и ссылаться на словарь,
 содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
 Создать класс Position (должность) на базе класса Worker.
 В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
 и дохода с учетом премии (get_total_income).

 Проверить работу примера на реальных данных
 (создать экземпляры класса Position, передать данные, проверить значения
 атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self._income = {"salary": 80000, "bonus": 25000}


class Position(Worker):
    def __init__(self, pos_name, name, surname):
        self.pos_name = pos_name
        super().__init__(name, surname)

    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_income(self):
        return sum(self._income.values())


unit1 = Position('Аналитик', 'Вася', 'Иванов')
print(unit1.get_full_name())
print(unit1.get_income())
print(unit1._income)
print(unit1.name)
