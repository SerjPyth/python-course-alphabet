from __future__ import annotations
from Car_class import Car, WrongException
from constants import *
import uuid
import random


class Garage:

    def __init__(self, town, cars, places, owner=None):
        self.town = town
        if self.town in TOWNS:
            self.town = town
        else:
            raise WrongException
        self.cars = cars if cars is not None else []
        self.places = int(places)
        self.owner = uuid.uuid4()

    def __contains__(self, item):
        return item in self.cars

    def __iter__(self):
        return self

    def __next__(self):

        if self.current < len(self.cars):
            res = self.cars[self.current]
            self.current += 1
            return res
        else:
            self.current = 0
            raise StopIteration

    def add_car(self, car):
        self.cars = []
        for _ in range(0, self.places):
            car = Car(
                price=random.randint(1000, 5000),
                type=random.choice(CARS_TYPES),
                producer=random.choice(CARS_PRODUCER),
                mileage=random.randint(1000, 15000)
            )
            self.cars.append(car)
            return self.cars

    def remove_car(self, car):
        if car in self.cars:
            car.remove(self.cars)
            return self.cars

    def hit_hat(self):
        return sum(Car.price, self.cars)


if __name__ == "__main__":

    a = random.choice(CARS_TYPES)
    # a2 = "Cart"
    # a = "Cart"
    b = random.choice(CARS_PRODUCER)
    # b = "Mercedes"
    c = random.randint(1000, 5000)
    d = random.randint(10000, 50000)
    f = 0
    g = uuid.uuid4()
    e = random.randint(1000, 15000)

aa = (Car(c, a, b, d, e))
# a2a = (Car(c, a2, b, d, e))


print(aa)
# print(a2a)

# print(Car.number_change(1))
# print(f, g)


