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
        self.garages = garages if garages is not None else []

    def __contains__(self, item):
        return item in self.garages



if __name__ == "__main__":
    car_types = ["SUV", "Truck", "Sedan", "Van", "Coupe", "Wagon", "Sports Car", "Diesel", "Crossover", "Luxury Car"]
    car_producer = ["BENTLEY", "BMW", "Bugatti", "Buick", "Chery", "Chevrolet", "Dodge", "Ford", "Lamborghini"]
    towns = ["Amsterdam", "Kyiv", "Prague", "Rome", "Paris", "London", "Berlin"]