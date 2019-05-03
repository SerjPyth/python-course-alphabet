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

    def hit_hat(self):
        return sum(Car.price, Garage.cars)

    def garage_count(self):
        for i in self.garages:
            i += 1
            return i

    def cars_count(self):
        cars_num = 0
        i = 0
        for i in self.garages:
            for Garage.cars in self.garages:
                cars_num += 1
            i += cars_num
        return i

    def add_car(self, car):
        if len(self.cars) < self.places:
            self.cars.append(car)
        else:
            print("No free space left!")
            raise WrongException


# if __name__ == "__main__":
