"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""

from __future__ import annotations
import uuid
from constants import *


class WrongException(Exception):
    pass


class Car:

    def __init__(self, price, type, producer, mileage):
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
        self.mileage = float(mileage)
        self.current = 0

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


class Cesar:

    def __init__(self, name, garages=None):
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
        return len(self.garages)

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
