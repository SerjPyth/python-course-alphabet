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
        if cars is None:
            self.cars = []
        else:
            self.cars = cars
        # self.cars = cars if cars is not None else []
        self.places = int(places)
        if owner is None:
            self.owner = None
        else:
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

    def __str__(self):
        return f"Hello. I`m a garage in {self.town} and I have {self.places} cars inside me. They are: {self.cars}. " \
            f"All of this is owned by {self.owner}."

    def add_car(self, car):
        if car not in self.cars:
            self.cars.append(car)

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)

    def hit_hat(self):
        return sum(Car.price, self.cars)


# if __name__ == "__main__":
a = random.choice(TOWNS)
# b = random.choice(CARS_PRODUCER)
# b = []
# b.add_car()
c = random.randint(2, 6)
d = 1
cars = []
for _ in range(0, c):
    car = Car(
        price=random.randint(1000, 5000),
        type=random.choice(CARS_TYPES),
        producer=random.choice(CARS_PRODUCER),
        number=uuid.uuid4(),
        mileage=random.randint(1000, 15000)
    )
    cars.append(car)


print(list(cars))
aa = (Garage(a, cars, c, d))
# print(aa)
aa.remove_car(cars[0])
# print(aa)
spec_car = Car(2566, "Van", "BMW", 1, 545)
aa.add_car(spec_car)
# print(spec_car)
print(aa)
# print(aa.hit_hat())
# a2a = (Garage(a, cars, c))
# a2a = (Car(c, a2, b, d, e))


# print(aa)
# print(a2a)

# print(Car.number_change(1))
# print(f, g)
