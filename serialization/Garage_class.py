from __future__ import annotations
from Car_class import Car, WrongException
from constants import *
import uuid
import random
import json
import pickle
import ruamel.yaml
import sys


class Garage:

    yaml_tag = u'!Garage'

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
        self.places = int(places)
        if owner is None:
            self.owner = None
        else:
            self.owner = uuid.uuid4()
        self.current = 0

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

    def __repr__(self):
        return "Garages('{}', '{}', {}, {})".format(self.town, self.cars, self.places, self.owner)

    def __setstate__(self, state):
        self.__dict__ = state

    def __getstate__(self):
        return self.__dict__

    def get_len_cars(self):
        return len(self.cars)

    def get_cars(self):
        return self.cars

    def get_places(self):
        return self.places

    def add_car(self, car):
        if len(self.cars) < self.places:
            self.cars.append(car)
        else:
            print("No free space left!")
            raise WrongException

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)

    def hit_hat(self):
        total = []
        i = self.places
        while i != 0:
            for car in self.cars:
                single = car.get_price()
                total.append(single)
                i -= 1
            return sum(total)

    @classmethod
    def to_yaml(cls, representer, node):
        return representer.represent_scalar(cls.yaml_tag, u'{.town}_{.cars}_{.places}_{.owner}'
                                            .format(node, node, node, node))

    @classmethod
    def from_yaml(cls, constructor, node):
        return cls(*node.value.split('_'))

    @classmethod
    def from_json(cls, data):
        town = data['town']
        cars = data['cars']
        places = data['places']
        owner = data['owner']
        gr = Garage(town=town, cars=str(cars), places=places, owner=str(owner))
        return gr

    @staticmethod
    def to_json(obj: Garage):
        data = {"town": obj.town, "cars": str(obj.cars), "places": obj.places, "owner": str(obj.owner)}
        return data


def from_json(data):
    town = data['town']
    cars = data['cars']
    places = data['places']
    owner = data['owner']
    gr = Garage(town=town, cars=str(cars), places=places, owner=str(owner))
    return gr


def to_json(obj: Garage):
    data = {"town": obj.town, "cars": str(obj.cars), "places": obj.places, "owner": str(obj.owner)}
    return data

# if __name__ == "__main__":
a = random.choice(TOWNS)
# b = random.choice(CARS_PRODUCER)
# b = []
# b.add_car()
c = random.randint(2, 6)
d = 1
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
aa = Garage(a, autos, c, d)
# print(pp.get_param())
# print(aa.hit_hat())
# print(aa.get_cars())
# aa.remove_car(autos[-1])
# print(len(aa.cars))
# print(aa)
# spec_car = Car(2566, "Van", "BMW", 1, 545)
# aa.add_car(spec_car)
# print(len(aa.cars))
print(aa)

if __name__ == "__main__":

    ser_gr = ''
    with open('data2.json', 'w') as file:
        # ser_pr = json.dump(autos, file, default=to_json)
        json.dump(aa, file, default=to_json, indent=4)
        print("Success")

    with open('data2.json') as f:
        load_ser_pr = json.load(f, object_hook=from_json)
        print(type(load_ser_pr), load_ser_pr)
    # except TypeError as e:
    #     print(e)

#     try:
#         load_pr = json.loads(ser_pr)
#         print(type(load_pr), load_pr)
#     except TypeError as e:
#         print(e)
#         #
#         # # Should work fine. Use custom hook
#     try:
#         load_pr = json.loads(ser_pr, object_hook=from_json)
#         print("Look here we have our programmer")
#         print(type(load_pr), load_pr)
#         print(load_pr.places)
#     except TypeError as e:
#         print(e)
#
#     try:
#         load_pr = json.loads(ser_pr, object_hook=from_json)
#         print("Look here we have our programmer")
#         print(type(load_pr), load_pr)
#         print(load_pr.town)
#     except TypeError as e:
#         print(e)
with open("data2.txt", "wb") as file:
    pickle.dump(aa, file)

# Lets load it
with open("data2.txt", "rb") as file:
    restore_obj = pickle.load(file)
    print(type(restore_obj), restore_obj)

yaml = ruamel.yaml.YAML()
yaml.register_class(Garage)
yaml.dump(aa, sys.stdout)
# with open("data2.yaml", "w") as file:
#     yaml.dump(aa, file)
#     print("Success!")
with open("data2.yaml", "r") as file:
    config = yaml.load(file)
    print(type(config), config)
# aaa = getattr(aa, "cars", "Some")
# bb = getattr(aaa, "price", "None")
# print(aaa)
# bbb = sum(map(lambda x: x.get('price'), dict(aaa)))
# print(bbb)
# print(Car.__dict__)
# print(aa.hit_hat())
# a2a = (Garage(a, cars, c))
# a2a = (Car(c, a2, b, d, e))


# print(aa)
# print(a2a)

# print(Car.number_change(1))
# print(f, g)
