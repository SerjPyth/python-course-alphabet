from __future__ import annotations
from Car_class import Car, WrongException
from Garage_class import Garage
from constants import *
import uuid
import random
import json
import pickle
import ruamel.yaml
import sys

class Cesar:

    yaml_tag = u'!Cesar'

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
        j = len(self.garages)
        while j != 0:
            for garage in self.garages:
                i += 1
                j -= 1
            return i

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
            for garage in self.garages:
                while garage.get_len_cars() < garage.get_places():
                    garage.get_cars().append(car)
            some_garage = garage.get_len_cars()
            min_garage = min(some_garage for garage in self.garages)
            min_garage.get_cars().append(car)
        else:
            print("No such garage in ownership")
            raise WrongException

    @classmethod
    def to_yaml(cls, representer, node):
        return representer.represent_scalar(cls.yaml_tag, u'{.name}_{.register_id}_{.garages}'
                                            .format(node, node, node))

    @classmethod
    def from_yaml(cls, constructor, node):
        return cls(*node.value.split('_'))

    @classmethod
    def from_json(cls, data):
        name = data['name']
        register_id = data['register_id']
        garages = data['garages']
        csr = Cesar(name=name, register_id=str(register_id), garages=str(garages))
        return csr

    @staticmethod
    def to_json(obj: Cesar):
        data = {"name": obj.name, "register_id": str(obj.register_id), "garages": str(obj.garages)}
        return data


def from_json(data):
    name = data['name']
    register_id = data['register_id']
    garages = data['garages']
    csr = Cesar(name=name, register_id=str(register_id), garages=str(garages))
    return csr


def to_json(obj: Cesar):
    data = {"name": obj.name, "register_id": str(obj.register_id), "garages": str(obj.garages)}
    return data

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
ces.add_car_ces(bb, spec_car)
# bb.add_car(spec_car)
print(ces)
print(ces.cars_count())
# if __name__ == "__main__":

    # ser_gr = ''
    # with open('data3.json', 'w') as file:
    #     # ser_pr = json.dump(autos, file, default=to_json)
    #     json.dump(ces, file, default=to_json, indent=4)
    #     print("Success")
    #
    # with open('data3.json') as f:
    #     load_ser_pr = json.load(f, object_hook=from_json)
    #     print(type(load_ser_pr), load_ser_pr)

# with open("data3.txt", "wb") as file:
#     pickle.dump(ces, file)
#
# # Lets load it
# with open("data3.txt", "rb") as file:
#     restore_obj = pickle.load(file)
#     print(type(restore_obj), restore_obj)
yaml = ruamel.yaml.YAML()
yaml.register_class(Cesar)
yaml.dump(ces, sys.stdout)
# with open("data3.yaml", "w") as file:
#     yaml.dump(ces, file)
#     print("Success!")
with open("data3.yaml", "r") as file:
    config = yaml.load(file)
    print(type(config), config)
