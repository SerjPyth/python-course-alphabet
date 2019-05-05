from __future__ import annotations
import uuid
import random
import pickle
import ruamel.yaml
from constants import *
import json
import sys
import json_utils


class WrongException(Exception):
    pass


class Car:

    yaml_tag = u'!Car'

    def __init__(self, price, type, producer, number, mileage):
        # self.price = str(float(price)) + "$"
        self.price = float(price)
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
        # self.mileage = str(float(mileage)) + " miles"
        self.current = 0
        self.mileage = float(mileage)

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

    def __setstate__(self, state):
        self.__dict__ = state

    def __getstate__(self):
        return self.__dict__

    def number_change(self):
        new_num = uuid.uuid4()
        self.number = new_num
        return self.number

    def get_price(self):
        return self.price

    @classmethod
    def to_yaml(cls, representer, node):
        return representer.represent_scalar(cls.yaml_tag, u'{.price}_{.type}_{.producer}_{.number}_{.mileage}'
                                            .format(node, node, node, node, node))
    @classmethod
    def from_yaml(cls, constructor, node):
        return cls(*node.value.split('_'))

    @classmethod
    def from_json(cls, data):
        price = data['price']
        type = data['type']
        producer = data['producer']
        number = data['number']
        mileage = data['mileage']
        cr = Car(price=int(price), type=type, producer=producer, number=str(number), mileage=mileage)
        return cr

    @staticmethod
    def to_json(obj: Car):
        data = {"price": obj.price, "type": obj.type, "producer": obj.producer,
                "number": str(obj.number), "mileage": obj.mileage}
        return data

#
def from_json(data):
    price = data['price']
    type = data['type']
    producer = data['producer']
    number = data['number']
    mileage = data['mileage']
    cr = Car(price=price, type=type, producer=producer, number=str(number), mileage=mileage)
    return cr


def to_json(obj: Car):
    data = {"price": obj.price, "type": obj.type, "producer": obj.producer, "number": str(obj.number), "mileage": obj.mileage}
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
# if __name__ == "__main__":


c = random.randint(2, 6)
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
# print(autos)
# print(auto.get_price())
if __name__ == "__main__":

    # ser_pr = ''
    # # try:
    with open('data.json', 'w') as file:
        json.dump(autos, file, default=to_json, indent=4)
        print("Success")
    #
    # load_ser_pr = ''
    # with open('data.json') as f:
    #     load_ser_pr = json.load(f, object_hook=from_json)
    #     print(type(load_ser_pr), load_ser_pr)
    # with open('data.json', 'w') as file:
    #     json.dump(autos, file, default=Car.to_json(autos), indent=4)
    #     print("Success")
    #     print(type(ser_pr), ser_pr)
    # except TypeError as e:
    #     print(e)

#     try:
#         load_pr = json.loads(ser_pr)
#         print(type(load_pr), load_pr)
#     except TypeError as e:
#         print(e)
#         #
#         # # Should works fine. Use custom hook
#     try:
#         load_pr = json.loads(ser_pr, object_hook=from_json)
#         print("Look here we have our programmer")
#         print(type(load_pr), load_pr)
#     except TypeError as e:
#         print(e)
#
#     try:
#         load_pr = json.loads(ser_pr, object_hook=from_json)
#         print("Look here we have our programmer")
#         print(type(load_pr), load_pr)
#     except TypeError as e:
#         print(e)
# Lets dump object to pickle
with open("data.txt", "wb") as file:
    pickle.dump(auto, file)
#
# Lets load it
with open("data.txt", "rb") as file:
    restore_obj = pickle.load(file)
    print(type(restore_obj), restore_obj)

yaml = ruamel.yaml.YAML()
yaml.register_class(Car)
yaml.dump(auto, sys.stdout)
# with open("data.yaml", "w") as file:
#     yaml.dump(auto, file)
#     print("Success!")
with open("data.yaml", "r") as file:
    config = yaml.load(file)
    print(type(config), config)
