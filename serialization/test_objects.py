import homework as hw
from constants import CARS_TYPES, CARS_PRODUCER, TOWNS
# from fixtures import car1, car2, car3, car4, car5, garage1, garage2, garage3, cesar_1, cesar_2
from fixtures import car4, car5, garage1, garage2, garage3, cesar_1, cesar_2
import uuid
import unittest


class CarTest(unittest.TestCase):

    def setUp(self) -> None:
        self.fake_car_type = ['bolid', 'Hatchback', 'Convertible', '', "some fake phrase", 12553, 1258964.65465421,
                              ["element_one", "element_two"], ("element_one", "element_two",),
                              {"element_one": "value_one", "element_two": "value_two"},
                              [], (), {}, None, True, False]

        self.fake_producers = ["DaeWoo", "McLaren", "just a string", "", 12553, 1258964.65465421,
                               ["element_one", "element_two"], ("element_one", "element_two",),
                               {"element_one": "value_one", "element_two": "value_two"},
                               [], (), {}, None, True, False]  # а ты правда продюсер?

        self.number = 'c4595999-28b9-4a98-bd85-9d59ada33efe'

        self.new_uuid_number = str(uuid.uuid4())

        self.bad_uuid_values_1 = ['35461654651-sadasd-szdfsf', '%4595999-28b9-4a98-bd85-9d59ada33efe',
                                  'c4595999-28b9-4a98-bd85-d59ada33efe', '', "some fake phrase"]

        self.bad_uuid_values_2 = [["element_one", "element_two"], ("element_one", "element_two",),
                                  {"element_one": "value_one", "element_two": "value_two"},
                                  [], (), {}, 12553, 1258964.65465421, uuid.uuid4(), True, False]

        self.bad_uuid_values_3 = [None]

        self.price_values = [12553, 1258964.65465421, "12553"]

        self.price_bad_values = [["element_one", "element_two"], ("element_one", "element_two",),
                                 {"element_one": "value_one", "element_two": "value_two"},
                                 [], (), {}, None, True, False]
        self.comparison = [1.0025, 100, 1000, 0, -1, 0.0, 100000000000000000, 10000000000000.0, 0.00000001, -1.0025]

        self.car1 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f53', car_type="Diesel",
                           producer="Ford")
        self.car2 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f53', car_type="Diesel",
                           producer="Ford")
        self.car3 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f55', car_type="Diesel",
                           producer="Ford", garage_numb=0)

    def tearDown(self) -> None:
        self.number = 'c4595999-28b9-4a98-bd85-9d59ada33efe'
        self.car1 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f53', car_type="Diesel",
                           producer="Ford")
        self.car2 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f53', car_type="Diesel",
                           producer="Ford")
        self.car3 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f55', car_type="Diesel",
                           producer="Ford", garage_numb=0)

    def test_car_type_checking_success(self):
        """This function will test  car type checking (if car type in CAR_TYPE list)"""
        for car_type in CARS_TYPES:
            self.assertEqual(hw.Car.type_checking(car_type), car_type)

    def test_car_type_checking_fail(self):
        """This function will test car type checking on wrong values"""
        for car_type in self.fake_car_type:
            with self.assertRaises(ValueError, msg="Type should be instance of CAR_TYPES!") as context:
                hw.Car.type_checking(car_type)
            self.assertTrue("Type should be instance of CAR_TYPES!" in context.exception.args)

    def test_car_producer_success(self):
        """This function will test  car producer checking (if car producer in CARS_PRODUCER list)"""
        for producer in CARS_PRODUCER:
            self.assertEqual(hw.Car.producer_checking(producer), producer)

    def test_car_producer_checking_fail(self):
        """This function will test car type checking on wrong values"""
        for producer in self.fake_producers:
            with self.assertRaises(ValueError, msg="Producer should be instance of CARS_PRODUCER!") as context:
                hw.Car.producer_checking(producer)
            self.assertTrue("Producer should be instance of CARS_PRODUCER!" in context.exception.args)

    def change_number(self, new_number):
        try:
            uuid.UUID(new_number, version=4)
            self.number = new_number
            return "Number has been changed"
        except ValueError or AttributeError or TypeError:
            return 'Sorry, you have entered wrong number'

    def test_change_number_success(self):
        """This function will test changing uuid-number of car function """
        expected_res = "Number has been changed"
        self.assertEqual(hw.Car.change_number(self, new_number=self.new_uuid_number), expected_res)
        self.assertEqual(self.number, self.new_uuid_number)

    def test_change_number_fail_attribute_error(self):
        """This function will test changing uuid-number of car function on wrong values: list, tuple, dict, float, int.
        Should be AttributeError"""
        expected_res = 'Sorry, you have entered wrong number. It should be a string, not list, tuple, set, dict, int or float'
        with self.assertRaises(AttributeError) as context:
            for value in self.bad_uuid_values_2:
                process = hw.Car.change_number(self, new_number=value)
                self.assertEqual(process, expected_res)
            self.assertTrue(
                'Sorry, you have entered wrong number. It should be a string, not list, tuple, set, dict, int or float'
                in context.exception.args)

    def test_change_number_fail_value_error(self):
        """This function will test changing uuid-number of car function on wrong values: bad string.
        Should be AttributeError"""
        expected_res = 'Sorry, you have entered bad format of string'
        with self.assertRaises(AttributeError) as context:
            for value in self.bad_uuid_values_1:
                process = hw.Car.change_number(self, new_number=value)
                self.assertEqual(process, expected_res)
            self.assertTrue("Sorry, you have entered bad format of string" in context.exception.args)

    def test_change_number_fail_type_error(self):
        """This function will test changing uuid-number of car function on wrong values: bad string.
        Should be AttributeError"""
        expected_res = 'Sorry, you have entered bad type of argument. ' \
                       'One of the hex, bytes, bytes_le, fields, or int arguments must be given'
        with self.assertRaises(AttributeError) as context:
            for value in self.bad_uuid_values_3:
                process = hw.Car.change_number(self, new_number=value)
                self.assertEqual(process, expected_res)
            self.assertTrue("Sorry, you have entered bad type of argument. "
                            "One of the hex, bytes, bytes_le, fields, or int arguments must be given"
                            in context.exception.args)

    def test_convert_to_float_success(self):
        """ This function will test convert to float function """
        for value in self.price_values:
            self.assertIsInstance(hw.Car._convert_to_float(value), float)
            self.assertEqual(hw.Car._convert_to_float(value), float(value))

    def test_convert_to_float_fail(self):
        """ This function will test convert to float function on bad data: str, list, dict, tuple, None, Bool"""
        for value in self.price_bad_values:
            self.assertEqual(hw.Car._convert_to_float(value), None)

    def test_equality_success(self):
        """This test will pass if two objects have the same attributes"""
        self.assertTrue(self.car1.equality(self.car2))

    def test_equality_fail_price(self):
        """This test will pass if two objects have NOT the same attribute price"""
        for value in self.comparison:
            self.car1.price = value
            self.assertFalse(self.car1.equality(self.car3))

    def test_equality_fail_mileage(self):
        """This test will pass if two objects have NOT the same attribute mileage"""
        for value in self.comparison:
            self.car1.mileage = value
            self.assertFalse(self.car1.equality(self.car3))

    def test_equality_fail_uuid(self):
        """This test will pass if two objects have NOT the same attribute uuid"""
        self.car1.uuid = uuid.uuid4()
        self.assertFalse(self.car1.equality(self.car3))

    def test_equality_fail_producer(self):
        """This test will pass if two objects have NOT the same attribute producer"""
        self.car1.producer = "Dodge"
        self.assertFalse(self.car1.equality(self.car3))

    def test_equality_fail_type(self):
        """This test will pass if two objects have NOT the same attribute car_type"""
        self.car1.car_type = "Coupe"
        self.assertFalse(self.car1.equality(self.car3))

    def test_equality_fail_garage(self):
        """This test will pass if two objects have NOT the same attribute garage numb"""
        self.car1.garage_numb = 1
        self.assertFalse(self.car1.equality(self.car3))

    def test_repr_success(self):
        """This func will test __repr__ of Car class on good value"""
        expected_res = 'Car(price=1.0, producer="Ford", car_type="Diesel", ' \
                       'number="65c11813-3eb5-4d48-b62b-3da6ef951f53", mileage=1.0, garage_numb=None)'
        self.assertIsInstance(self.car1.__repr__(), str)
        self.assertEqual(self.car1.__repr__(), expected_res)

    def test_repr_fail(self):
        """This func will test __repr__ of Car class on bad value"""
        expected_res = 'CAR(price=1.0, producer="Ford", car_type="Diesel", ' \
                       'number="65c11813-3eb5-4d48-b62b-3da6ef951f53", mileage=1.0, garage_numb=None)'
        self.assertIsInstance(self.car1.__repr__(), str)
        self.assertFalse(self.car1.__repr__() == expected_res)

    def test_str_success(self):
        """This func will test __str__ of Car class on good value"""
        expected_res = "This car has attributes: {'price': 1.0, 'number': '65c11813-3eb5-4d48-b62b-3da6ef951f53', " \
                       "'mileage': 1.0, 'garage_numb': None, 'producer': 'Ford', 'car_type': 'Diesel'}"
        self.assertIsInstance(self.car1.__str__(), str)
        self.assertEqual(self.car1.__str__(), expected_res)

    def test_str_fail(self):
        """This func will test __str__ of Car class on bad value"""
        expected_res = "BAD car has attributes: {'price': 1.0, 'number': '65c11813-3eb5-4d48-b62b-3da6ef951f53', " \
                       "'mileage': 1.0, 'garage_numb': None, 'producer': 'Ford', 'car_type': 'Diesel'}"
        self.assertIsInstance(self.car1.__str__(), str)
        self.assertFalse(self.car1.__str__() == expected_res)


class GarageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.converted_values = [12553, 1258964.65465421, "12553"]

        self.converted_fail = [["element_one", "element_two"], ("element_one", "element_two",),
                                 {"element_one": "value_one", "element_two": "value_two"},
                                 [], (), {}, True, False,  None]

        self.uuid_number = 'c4595999-28b9-4a98-bd85-9d59ada33efe'
        self.uuid_bad_number = 'c4595999-28b9-4a98-bd85-9d59ada33ef'

        self.change_owner_number = [None, self.uuid_number]

        self.bad_towns = ['Zdolbuniv', 'Irpin', 'Ivachkiv',
                          ["element_one", "element_two"], ("element_one", "element_two",),
                          {"element_one": "value_one", "element_two": "value_two"},
                          [], (), {}, True, False, None]

        self.free_places = 15

        self.car1 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f53', car_type="Diesel",
                           producer="Ford")
        self.car2 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f53', car_type="Diesel",
                           producer="Ford", )
        self.car3 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f55', car_type="Diesel",
                           producer="Ford", garage_numb=None)
        self.car4 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f55', car_type="Diesel",
                           producer="Ford", garage_numb=4)
        self.car5 = hw.Car(price=15, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f57', car_type="Diesel",
                           producer="Ford", garage_numb=5)
        self.car6 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f58', car_type="Diesel",
                           producer="Ford", garage_numb=5)



        self.garage1 = hw.Garage(15, 'Amsterdam', self.car1,  owner='be23adf5-3d7f-43f1-9874-e60d61c84522', number=1,)
        self.garage2 = hw.Garage(15, 'Kiev', self.car3, owner='be23adf5-3d7f-43f1-9874-e60d61c84523', number=2)
        self.garage3 = hw.Garage(places=15, owner='be23adf5-3d7f-43f1-9874-e60d61c84524', number=3, town='Prague')
        self.garage4 = hw.Garage(places=0, owner='be23adf5-3d7f-43f1-9874-e60d61c84525', number=4, town='Prague')
        self.garage5 = hw.Garage(15, 'Amsterdam', self.car5, self.car6, owner='be23adf5-3d7f-43f1-9874-e60d61c84522', number=5)


        self.new_uuid_number = str(uuid.uuid4())

        self.bad_uuid_values_1 = ['35461654651-sadasd-szdfsf', '%4595999-28b9-4a98-bd85-9d59ada33efe',
                                  'c4595999-28b9-4a98-bd85-d59ada33efe', '', "some fake phrase"]

        self.bad_uuid_values_2 = [["element_one", "element_two"], ("element_one", "element_two",),
                                  {"element_one": "value_one", "element_two": "value_two"},
                                  [], (), {}, 12553, 1258964.65465421, uuid.uuid4(), True, False]

        self.bad_uuid_values_3 = [None]


    def tearDown(self) -> None:
        self.car1 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f53', car_type="Diesel",
                           producer="Ford")
        self.car2 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f53', car_type="Diesel",
                           producer="Ford", garage_numb=None)
        self.car3 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f55', car_type="Diesel",
                           producer="Ford", garage_numb=2)

        self.car4 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f56', car_type="Diesel",
                           producer="Ford", garage_numb=4)
        self.car5 = hw.Car(price=15, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f57', car_type="Diesel",
                           producer="Ford", garage_numb=5)
        self.car6 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f58', car_type="Diesel",
                           producer="Ford", garage_numb=5)

        self.garage1 = hw.Garage(15, 'Amsterdam', self.car1,  owner='be23adf5-3d7f-43f1-9874-e60d61c84522', number=1,)
        self.garage2 = hw.Garage(15, 'Kiev', self.car3, owner='be23adf5-3d7f-43f1-9874-e60d61c84523', number=2)
        self.garage3 = hw.Garage(places=15, owner='be23adf5-3d7f-43f1-9874-e60d61c84524', number=3, town='Prague')
        self.garage4 = hw.Garage(places=0, owner='be23adf5-3d7f-43f1-9874-e60d61c84524', number=4, town='Prague')


    def test_to_int_success(self):
        """This func will test to init convert_func on good value"""
        for value in self.converted_values:
            self.assertIsInstance(hw.Garage._to_int(value), int)
            self.assertEqual(hw.Garage._to_int(value), int(value))

    def test_to_int_fail(self):
        """This func will test to init convert_func on bad value"""
        for value in self.converted_fail:
            self.assertEqual(hw.Garage._to_int(value), None)

    def test_owner_checking_success(self):
        """This func will test owner checking func on good value"""
        self.assertEqual(hw.Garage.owner_checking(self.change_owner_number[0]), None)
        self.assertEqual(hw.Garage.owner_checking(self.change_owner_number[1]), self.change_owner_number[1])

    def test_owner_checking_fail(self):
        """This func will test owner checking func on bad value"""
        for value in self.converted_fail[:-1]:
            expected_res = 'Sorry, you have entered wrong number. ' \
                       'It should be a string, not list, tuple, set, dict, int or float'
            self.assertEqual(hw.Garage.owner_checking(value), expected_res)
        expected_res_2 = 'Sorry, you have entered bad format of string'
        self.assertEqual(hw.Garage.owner_checking(self.uuid_bad_number), expected_res_2)

    def test_town_checking_success(self):
        """This func will test town checking func on good value"""
        for town in TOWNS:
            self.assertEqual(hw.Garage.town_checking(town), town)

    def test_town_checking_fail(self):
        """This func will test town checking func on bad value"""
        with self.assertRaises(ValueError) as context:
            for town in self.bad_towns:
                hw.Garage.town_checking(town)
            self.assertTrue('Town should be instance of TOWNS!' in context.exception.args)


    def test_add_car_to_garage_success(self):
        """This func will test add car func on good value"""
        self.assertTrue(self.garage1.free_places() > 0)
        self.assertTrue(self.car2.garage_numb is None)
        expected_res = "Car has been added"
        self.assertEqual(self.garage1.add(self.car2), expected_res)
        self.assertEqual(self.car2.garage_numb, 1)

    def test_add_car_to_garage_fail(self):
        """This func will test add car func on bad value"""
        with self.assertRaises(ValueError) as context:
            self.garage1.add(self.car4)
        expected_res_1 = "This car is already in other garage"
        self.assertTrue(expected_res_1 in context.exception.args)
        with self.assertRaises(ValueError) as context:
            self.garage4.add(self.car1)
        expected_res_2 = "Sorry, this garage is full. Car has not been changed"
        self.assertTrue(expected_res_2 in context.exception.args)

    def test_remove_car_from_garage_success(self):
        """This func will test remove func on good value"""
        expected_res = "Car has been removed"
        self.assertEqual(self.garage1.remove(self.car1), expected_res)
        self.assertEqual(self.car1.garage_numb, None)
        self.assertEqual(self.garage2.remove(self.car3), expected_res)
        self.assertEqual(self.car3.garage_numb, None)

    def test_remove_car_from_garage_fail(self):
        """This func will test remove car func on bad value"""
        with self.assertRaises(ValueError) as context:
            self.garage1.remove(car4)
        expected_res = "Sorry, there is no that car in the garage"
        self.assertTrue(expected_res in context.exception.args)

    def test_hit_hat_success(self):
        """This func will test hit_hat func on good value"""
        self.assertEqual(self.garage1.hit_hat(), 1.0)
        self.assertEqual(self.garage5.hit_hat(), 16.0)

    def test_change_owner_success(self):
        """This func will test change_owner func on good value"""
        pass

    def test_change_owner_fail(self):
        """This func will test change_owner func on bad value"""
        pass

    def test_free_places_success(self):
        """This func will test free_places func on good value"""
        pass

    def test_free_places_fail(self):
        """This func will test free_places func on bad value"""
        pass

    def test_str_success(self):
        """This func will test __str__ of Garage class on good value"""

        expected_res_1 = """Garage 1 has next attributes:
        cars = '1 cars', 
        owner = 'be23adf5-3d7f-43f1-9874-e60d61c84522',
        town = 'Amsterdam',
        number = '1',
        free places = 14
        """
        expected_res_2 = """Garage 2 has next attributes:
        cars = '1 cars', 
        owner = 'be23adf5-3d7f-43f1-9874-e60d61c84523',
        town = 'Kiev',
        number = '2',
        free places = 14
        """
        self.assertEqual(self.garage1.__str__(), expected_res_1)
        self.assertEqual(self.garage2.__str__(), expected_res_2)

    def test_str_fail(self):
        """This func will test __str__ of Garage class on bad value"""

        expected_res_1 = """Garage 1 has next attributes:
        cars = '2 cars', 
        owner = 'e23adf5-3d7f-43f1-9874-e60d61c84522',
        town = 'Amsterdam',
        number = '1',
        free places = 13
        """
        expected_res_2 = """Garage 2 has next attributes:
        cars = '1 cars', 
        owner = 'e23adf5-3d7f-43f1-9874-e60d61c84523',
        town = 'Kiev',
        number = '2',
        free places = 14
        """
        self.assertFalse(self.garage1.__str__() == expected_res_1)
        self.assertFalse(self.garage2.__str__() == expected_res_2)

    def test_repr_success(self):
        """This func will test __repr__ of Garage class on good value"""
        expected_res_1 =  """Garage("{'places': 15, 'owner': 'be23adf5-3d7f-43f1-9874-e60d61c84522', 'number': 1, 'cars': [Car(price=1.0, producer="Ford", car_type="Diesel", number="65c11813-3eb5-4d48-b62b-3da6ef951f53", mileage=1.0, garage_numb=None)], 'town': 'Amsterdam'}")"""

        expected_res_2 = """Garage("{'places': 15, 'owner': 'be23adf5-3d7f-43f1-9874-e60d61c84523', 'number': 2, 'cars': [Car(price=1.0, producer="Ford", car_type="Diesel", number="65c11813-3eb5-4d48-b62b-3da6ef951f55", mileage=1.0, garage_numb=None)], 'town': 'Kiev'}")"""
        self.assertEqual(self.garage1.__repr__(), expected_res_1)
        self.assertEqual(self.garage2.__repr__(), expected_res_2)



    def test_repr_fail(self):
        """This func will test __repr__ of Garage class on bad value"""
        expected_res_1 = """Garage("{'places': 1, 'owner': 'be23adf5-3d7f-43f1-9874-e60d61c84522', 'number': 1, 'cars': [Car(price=1.0, producer="Ford", car_type="Diesel", number="65c11813-3eb5-4d48-b62b-3da6ef951f53", mileage=1.0, garage_numb=None), Car(price=1.0, producer="Ford", car_type="Diesel", number="65c11813-3eb5-4d48-b62b-3da6ef951f53", mileage=1.0, garage_numb=None)], 'town': 'Amsterdam'}")"""

        expected_res_2 = """Garage("{'places': 1, 'owner': 'be23adf5-3d7f-43f1-9874-e60d61c84523', 'number': 2, 'cars': [Car(price=1.0, producer="Ford", car_type="Diesel", number="65c11813-3eb5-4d48-b62b-3da6ef951f55", mileage=1.0, garage_numb=None)], 'town': 'Kiev'}")"""
        self.assertFalse(self.garage1.__repr__() == expected_res_1)
        self.assertFalse(self.garage2.__repr__() == expected_res_2)


class CesarTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_garages_checking_success(self):
        """This func will test if garage isn't belong to other cesar on good value"""
        pass

    def test_garages_checking_fail(self):
        """This func will test if garage isn't belong to other cesar on bad value"""
        pass

    def test_garages_count_success(self):
        """This func will test count number of garages on good values"""
        pass

    def test_garages_count_fail(self):
        """This func will test count number of garages on bad values"""
        pass

    def test_hit_hat_success(self):
        """This func will test summary price of garages on good values"""
        pass

    def test_hit_hat_fail(self):
        """This func will test summary price of garages on bad values"""
        pass

    def test_cars_count_success(self):
        """This func will test count of cars in all garages on good values"""
        pass

    def test_cars_count_fail(self):
        """This func will test count of cars in all garages on bad values"""
        pass

    def test_add_car_success(self):
        """This func will test car adding to garage on good value"""
        pass

    def test_add_car_fail(self):
        """This func will test car adding to garage on bad value"""
        pass

    def test_str_success(self):
        """This func will test __str__ of Garage class on good value"""
        pass

    def test_str_fail(self):
        """This func will test __str__ of Garage class on bad value"""
        pass

    def test_rept_success(self):
        """This func will test __repr__ of Garage class on good value"""
        pass

    def test_rept_fail(self):
        """This func will test __repr__ of Garage class on bad value"""
        pass

class JsonConverterTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_default_car_success(self):
        """This func will test car serialization func on good value"""
        pass

    def test_default_garage_success(self):
        """This func will test garage serialization func on good value"""
        pass

    def test_default_cesar_success(self):
        """This func will test cesar serialization func on good value"""
        pass

    def test_default_car_fail(self):
        """This func will test car serialization func on bad value"""
        pass

    def test_default_garage_fail(self):
        """This func will test garage serialization func on bad value"""
        pass

    def test_default_cesar_fail(self):
        """This func will test cesar serialization func on bad value"""
        pass

class DeserailizationTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_car_deserial_success(self):
        """This func will test car deserialization func on good value"""
        pass

    def test_garage_deserial_success(self):
        """This func will test garage deserialization func on good value"""
        pass

    def test_cesar_deserial_success(self):
        """This func will test cesar deserialization func on good value"""
        pass

    def test_car_deserial_fail(self):
        """This func will test car deserialization func on bad value"""
        pass

    def test_garage_deserial_fail(self):
        """This func will test garage deserialization func on bad value"""
        pass

    def test_cesar_deserial_fail(self):
        """This func will test cesar deserialization func on bad value"""
        pass

    def test_json_hook_fail(self):
        """This func will test json_hook func on good value"""
        pass

    def test_json_hook_fail(self):
        """This func will test json_hook func on bad value"""
        pass


if __name__ == "__main__":
    unittest.main()