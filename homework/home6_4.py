"""
Lesson 6. Task 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, color: str, name: str, is_police: bool = False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car is moving')

    def stop(self):
        print('Car stopped')

    def turn(self, direction):
        if direction in ('left', 'right'):
            print(f'Car turned to {direction}')
        else:
            raise ValueError('direction can be "right" or "left"')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print("Speed is very high")


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print("Speed is very high")


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)


s_c = SportCar('Yellow', 'Ford_GT')
print(s_c.is_police)
print(s_c.name)
s_c.go()
s_c.speed = 90
s_c.show_speed()

w_c = WorkCar('Black', 'Mercedes_V')
print(w_c.name)
w_c.go()
w_c.turn('left')
w_c.speed = 46
w_c.show_speed()
