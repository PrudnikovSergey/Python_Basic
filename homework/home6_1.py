import time
from itertools import cycle


class TrafficLight:
    __modes = (('Red', 7), ('Yellow', 2), ('Green', 9), ('Yellow', 2))
    __light_start = 0
    __next_light = 0

    def __init__(self):
        self.__color = self.__modes[0][0]
        self.__light_start = time.time()
        self.__tic()

    def __tic(self):
        """
        В зависимости от предыдущего времени переключаем свет светофора
        При этом не предполагается блокировка Sleep
        :return: str
        """
        if self.__light_start + dict(self.__modes)[self.__color] <= time.time():
            self.__color, self.__light_start = (self.__modes[self.__next_light][0], time.time())
            self.__next_light = (
                self.__next_light + 1
                if len(self.__modes) > self.__next_light
                else 0
            )

    def color(self):
        self.__tic()
        return self.__color


if __name__ == "__main__":
    lighter = TrafficLight()
    time.sleep(0.1)
    lighter_2 = TrafficLight()
    time.sleep(0.1)
    lighter_3 = TrafficLight()
    time.sleep(0.1)
    for light in cycle((lighter, lighter_2, lighter_3)):
        print(light.color())
        time.sleep(0.5)
