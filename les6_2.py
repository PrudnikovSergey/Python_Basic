import random

class Car:
    __population = []

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        self.vin = f'{self.brand[0]}-' \
                   f'{random.randint(random.randint(1, 1000), random.randint(1000, 10000))}-' \
                   f'{self.color[0]}-{random.randint(random.randint(1, 1000), random.randint(5000, 15000))}'
        self.__population.append(self)

    def get_population(self):
        return tuple(self.__population)


class CarFactory:
    __products = []

    def __init__(self, brand, colors, name):
        self.brand = brand
        self.colors = colors
        self.name = name

    def create_car(self, count):
        products = [Car(random.choice(self.colors),
                    self.brand,
                    ) for _ in range(count)]
        self.__products.extend(products)
        return products


car_1 = Car('White', 'Ford')
car_2 = Car('Red', 'Tesla')

factory = CarFactory('Ford', ['White', 'Blue', 'Red', 'Black'], 'FordFactory')
cars = factory.create_car(10)
print(1)
factory.colors.append('Green')
cars2 = factory.create_car(10)
print(1)
factory.brand = 'Tesla'
cars3 = factory.create_car(10)
print(1)