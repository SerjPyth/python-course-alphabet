"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно


Advanced
Добавити опрацьовку формату ini

"""

from __future__ import annotations
import uuid
from constants import *


class WrongException(Exception):
    pass


class Car:

    yaml_tag = u'!Car'

    def __init__(self, price, type, producer, mileage, number=None):

        self.price = self._convert_to_float(price)
        self.type = self.type_checking(type)
        self.producer = self.producer_checking(producer)
        self.number = uuid.uuid4() if number is None else number
        self.current = 0
        self.mileage = self._convert_to_float(mileage)

    @staticmethod
    def _convert_to_float(value):
        try:
            if value is True or value is False:
                raise TypeError
            return float(value)
        except TypeError:
            return None

    @staticmethod
    def type_checking(type):
        if type in CARS_TYPES:
            return type
        else:
            raise ValueError("Type should be an instance of CAR_TYPES! Please, reconsider.")

    @staticmethod
    def producer_checking(producer):
        if producer in CARS_PRODUCER:
            return producer
        else:
            raise ValueError("Producer should be an instance of CARS_PRODUCER! When will you learn?")

    def equality(self, another):
        return vars(self) == vars(another)

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

    def number_change(self, new_number):
        uuid.UUID(new_number, version=4)
        self.number = new_number
        return "Number has been successfully changed"

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
        cr = Car(price=price, type=type, producer=producer, number=str(number), mileage=mileage)
        return cr

    @staticmethod
    def to_json(obj: Car):
        data = {"price": obj.price, "type": obj.type, "producer": obj.producer,
                "number": str(obj.number), "mileage": obj.mileage}
        return data


class Garage:

    yaml_tag = u'!Garage'

    def __init__(self, town, *cars, places, owner=None):
        self.town = self.town_check(town)
        self.cars = [car for car in cars]
        self.places = self._convert_to_int(places)
        self.owner = self.owner_check(owner)
        self.current = 0

    @staticmethod
    def owner_check(owner):
        if owner is None:
            return owner
        else:
            try:
                uuid.UUID(owner, version=4)
                return owner
            except AttributeError:
                return 'You failed! Try again with a string.'
            except ValueError:
                return 'Failed again! Google how uuid should look like.'


    @staticmethod
    def town_check(town):
        if town in TOWNS:
            return town
        else:
            raise ValueError("Town should be instance of TOWNS! Treat yourself with a bit of geography")

    @staticmethod
    def _convert_to_int(value):
        try:
            if value is True or value is False:
                raise TypeError
            return int(value)
        except TypeError:
            return None

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

    def free_place(self):
        return self.places - len(self.cars)

    def add_car(self, car):
        if len(self.cars) < self.places:
            self.cars.append(car)
            return "Car has been added."
        else:
            raise ValueError("No free space left!")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            return "You just deleted that car."
        else:
            return "No such car."

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
