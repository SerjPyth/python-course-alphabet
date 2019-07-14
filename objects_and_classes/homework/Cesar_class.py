from __future__ import annotations
from Car_class import Car, WrongException
from Garage_class import Garage
from constants import *
import uuid
import random


class Cesar:

    def __init__(self, name, register_id, garages=None):
        self.name = str(name)
        self.register_id = uuid.uuid4()
        if garages is None:
            self.garages = []
        else:
            self.garages = garages

    def __contains__(self, item):
        return item in self.garages

    def __str__(self):
        return f"Hello. I`m a philanthropist, billionaire {self.name} and my ID is {self.register_id}. " \
            f"I`m a proud owner of this cuties: {self.garages}."

    def __repr__(self):
        return "Cesar('{}', {}, '{}')".format(self.name, self.register_id, self.garages)

    def __setstate__(self, state):
        self.__dict__ = state

    def __getstate__(self):
        return self.__dict__

    def total_hit_hat(self):
        total = []
        i = len(self.garages)
        while i != 0:
            for garage in self.garages:
                single = garage.hit_hat()
                total.append(single)
                i -= 1
            return sum(total)

    def garage_count(self):
        i = 0
        # j = len(self.garages)
        j = len(str(self.garages))
        while j != 0:
            for garage in self.garages:
                i += 1
                j -= 1
            return i

    # def cars_count(self):
    #     cars_num = 0
    #     i = 0
    #     j = len(self.garages)
    #     k = len(Garage.cars)
    #     while j != 0:
    #         for garage in self.garages:
    #             while k != 0:
    #                 for garage.cars in self.garages:
    #                     cars_num += 1
    #                     k -= 1
    #             j -= 1
    #             i += cars_num
    #     return i
    #
    # def cars_count(self):
    #     i = 0
    #     cars_num = 0
    #     for garage in self.garages:
    #         for garage in self.garages:
    #             cars_num += garage.get_cars()
    #         i += cars_num
    #         g = cars_num/3
    #     return int(g)

    def cars_count(self):
        cars_num = 0
        for garage in self.garages:
            cars_num += garage.get_len_cars()
        return cars_num

    def add_car_ces(self, garage, car):
        if garage in self.garages:
            if garage.get_len_cars() < garage.get_places():
                garage.get_cars().append(car)
            else:
                print("No free space left!")
                raise WrongException
        elif garage is None:
            garage.get_cars().append(car)
            # for garage in self.garages:
            #     while garage.get_len_cars() < garage.get_places():
            #         garage.get_cars().append(car)
            # some_garage = garage.get_len_cars()
            # min_garage = min(some_garage for garage in self.garages)
            # min_garage.get_cars().append(car)
        else:
            print("No such garage in ownership")
            raise WrongException

    # def add_car_ces(self, garage, car):
    #     for garage in self.garages:
    #         if garage in self.garages:
    #             garage.get_cars().append(car)
    #         elif garage is None:
    #             while garage.get_len_cars() < garage.get_places():
    #                 garage.get_cars().append(car)
    #         # some_garage = garage.get_len_cars()
    #         # min_garage = min(some_garage for garage in self.garages)
    #         # min_garage.get_cars().append(car)
    #         elif garage.get_len_cars() > garage.get_places():
    #             print("No such garage in ownership")
    #             raise WrongException
    #         else:
    #             print("No such garage in ownership")
    #             raise WrongException


a = random.choice(TOWNS)
# c = random.randint(2, 6)
d = 1
c = 2
autos = []
for _ in range(0, c):
    auto = Car(
        price=random.randint(1000, 5000),
        type=random.choice(CARS_TYPES),
        producer=random.choice(CARS_PRODUCER),
        number=uuid.uuid4(),
        mileage=random.randint(1000, 15000)
    )
    autos.append(auto)
c1 = 2
autos1 = []
for _ in range(0, c1):
    auto1 = Car(
        price=random.randint(1000, 5000),
        type=random.choice(CARS_TYPES),
        producer=random.choice(CARS_PRODUCER),
        number=uuid.uuid4(),
        mileage=random.randint(1000, 15000)
    )
    autos1.append(auto1)

print(autos)
print(autos1)
aa = Garage(a, autos, c, d)
bb = Garage(a, autos1, c1, d)
ff = Garage(a, autos, c, d)
dd = Garage(a, autos1, c1, d)
cc = [aa, bb, ff]
n = "Pablo"
ces = Cesar(n, 1, cc)
print(ces)
print(ces.garage_count())
print(ces.cars_count())
print(ces.total_hit_hat())
bb.remove_car(autos1[0])
print(ces.cars_count())
spec_car = Car(2566, "Van", "BMW", 1, 545)
# ces.add_car_ces(garage=None, car=spec_car)
# bb.add_car(spec_car)
print(ces)
print(ces.cars_count())
