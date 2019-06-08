import homework
from constants import CARS_TYPES, CARS_PRODUCER, TOWNS
import uuid
import unittest


class CarTest(unittest.TestCase):

    def setUp(self) -> None:
        self.fake