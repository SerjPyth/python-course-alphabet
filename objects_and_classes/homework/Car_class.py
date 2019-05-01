from __future__ import annotations
import uuid
# import random
from constants import *
import json


class WrongException(Exception):
    pass


class Car:

    def __init__(self, price, type, producer, number, mileage):
        self.price = str(float(price)) + "$"
        self.type = type
        if self.type in CARS_TYPES:
            self.type = type
        else:
            raise WrongException
        self.producer = producer
        if self.producer in CARS_PRODUCER:
            self.producer = producer
        else:
            raise WrongException
        self.number = uuid.uuid4()
        self.mileage = str(float(mileage)) + " miles"

    def __iter__(self):
        return self

    def __next__(self):

        if self.current < len(self.type):
            res = self.type[self.current]
            self.current += 1
            return res
        else:
            self.current = 0
            raise StopIteration

    def __eq__(self, other: Car):
        return self.price == other.price

    def __ne__(self, other: Car):
        return self.price != other.price

    def __le__(self, other: Car):
        return self.price <= other.price

    def __lt__(self, other: Car):
        return self.price < other.price

    def __gt__(self, other: Car):
        return self.price > other.price

    def __ge__(self, other: Car):
        return self.price >= other.price

    def __str__(self):
        return f"Hello. My name is {self.type} {self.number} and I am from {self.producer} manufacturer. " \
            f"My price is {self.price} while I ran for about {self.mileage}."

    def __repr__(self):
        return "Car({}, '{}', '{}', {}, {})".format(self.price, self.type, self.producer, self.number, self.mileage)

    def number_change(self):
        new_num = uuid.uuid4()
        self.number = new_num
        return self.number

    @classmethod
    def from_json(cls, data):
        price = data['price']
        type = data['type']
        producer = data['producer']
        number = data['number']
        mileage = data['mileage']
        cr = Car(price=price, type=type, producer=producer, number=number, mileage=mileage)
        return cr

    @staticmethod
    def to_json(obj: Car):
        data = {"price": obj.price, "type": obj.type, "producer": obj.producer,
                "number": obj.number, "mileage": obj.mileage}
        return data

# a = random.choice(CARS_TYPES)
# b = random.choice(CARS_PRODUCER)
# c = random.randint(1000, 5000)
# d = random.randint(10000, 50000)
# f = 0
# g = uuid.uuid4()
# e = random.randint(1000, 15000)
#
# car_1 = Car(c, a, b, d, e)
#
# print(car_1)
#
# car_1.number_change()
#
# print(car_1)
#
# car_1.number_change()
#
# print(car_1)
