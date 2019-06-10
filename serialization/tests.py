import homework as hw
from constants import CARS_TYPES, CARS_PRODUCER, TOWNS
import uuid
import unittest


class CarTest(unittest.TestCase):

    def setUp(self) -> None:
        self.fake_type = ["mini", "Halfvagon", "Chromed", "", "raw data", 123444, 237452734.23423,
                              ["item_one", "item_two"], ("item_one", "item_two",),
                              {"item_one": "value_one", "item_two": "value_two"},
                              [], (), {}, None, True, False]

        self.fake_producers = ["Hyundai", "Lada", "", "string", 123444, 237452734.2,
                               ["item_one", "item_two"], ("item_one", "item_two",),
                               {"item_one": "value_one", "item_two": "value_two"},
                               [], (), {}, None, True, False]

        self.number = 'v1237353-32n5-5m23-jh84-8u34mfd5dfd'

        self.new_number = str(uuid.uuid4())

        self.bad_uuid_1 = ['1324812871-alfwewqwq-qweqweqww', '#123751-sd63h-13241-sd623h-d27324323hj',
                           '45t45645g45g-464g4g56-4564g54-4564ererre', '', 'fake']

        self.price_values = [12314, 331231.1231, '12412']

        self.price_bad_values = [["item_one", "item_two"], ("item_one", "item_two",),
                                 {"item_one": "value_one", "item_two": "value_two"},
                                 [], (), {}, None, True, False]

        self.comparison = [1.255, 100, 1000, 0, -1, 0.0, 100000000000000, 1000000000000000.0, 0.0000001, -1.255]

        self.car1 = hw.Car(price=1, type="Coupe", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=1)

        self.car2 = hw.Car(price=1, type="Coupe", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=1)

        self.car3 = hw.Car(price=1, type="Coupe", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=1)

    def tearDown(self) -> None:
        self.number = 'c4595999-28b9-4a98-bd85-9d59ada33efe'

        self.car1 = hw.Car(price=1, type="Coupe", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=1)

        self.car2 = hw.Car(price=1, type="Coupe", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=1)

        self.car3 = hw.Car(price=1, type="Coupe", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=1)

    def test_car_type_checking_success(self):
        for type in CARS_TYPES:
            self.assertEqual(hw.Car.type_checking(type), type)

    def test_car_type_checking_failure(self):
        for type in self.fake_type:
            with self.assertRaises(ValueError, msg="Type should be an instance of CAR_TYPES! "
                                                   "Please, reconsider.") as context:
                hw.Car.type_checking(type)
            self.assertTrue("Type should be an instance of CAR_TYPES! Please, reconsider." in context.exception.args)

    def test_car_producer_checking_success(self):
        for producer in CARS_PRODUCER:
            self.assertEqual(hw.Car.producer_checking(producer), producer)

    def test_car_producer_checking_failure(self):
        for producer in self.fake_producers:
            with self.assertRaises(ValueError, msg="Producer should be an instance of CARS_PRODUCER!"
                                                   " When will you learn?") as context:
                hw.Car.producer_checking(producer)
            self.assertTrue("Producer should be an instance of CARS_PRODUCER! When will you learn?" in context.exception.args)

    def test_number_change_success(self):
        expected_res = "Number has been successfully changed"
        self.assertEqual(hw.Car.number_change(self, new_number=self.new_number), expected_res)
        self.assertEqual(self.number, self.new_number)

    def test_convert_to_float_success(self):
        for i in self.price_values:
            self.assertIsInstance(hw.Car._convert_to_float(i), float)
            self.assertEqual(hw.Car._convert_to_float(i), float(i))

    def test_convert_to_float_failure(self):
        for i in self.price_bad_values:
            self.assertEqual(hw.Car._convert_to_float(i), None)

    def test_equality_success(self):
        self.assertTrue(self.car1.equality(self.car2))

    def test_equality_failure_price(self):
        for value in self.comparison:
            self.car1.price = value
            self.assertFalse(self.car1.equality(self.car3))

    def test_equality_failure_mileage(self):
        for value in self.comparison:
            self.car1.mileage = value
            self.assertFalse(self.car1.equality(self.car3))

    def test_equality_failure_uuid(self):
        self.car1.uuid = uuid.uuid4()
        self.assertFalse(self.car1.equality(self.car3))

    def test_equality_failure_producer(self):
        self.car1.producer = "BMW"
        self.assertFalse(self.car1.equality(self.car3))

    def test_equality_failure_type(self):
        self.car1.type = "Van"
        self.assertFalse(self.car1.equality(self.car3))

    def test_repr_success(self):
        expected_res = "Car(1.0, 'Coupe', 'Bugatti', 65c11813-3eb5-4d48-b62b-3da6ef951f53, 1.0)"
        self.assertIsInstance(self.car1.__repr__(), str)
        self.assertEqual(self.car1.__repr__(), expected_res)

    def test_repr_failure(self):
        expected_res = "Car('1.0', 'Coupe', 'Bugatti', 65c11813-3eb5-4d48-b62b-3da6ef951f53, 1.0)"
        self.assertIsInstance(self.car1.__repr__(), str)
        self.assertFalse(self.car1.__repr__() == expected_res)

    def test_str_success(self):
        expected_res = "Hello. My name is Coupe 65c11813-3eb5-4d48-b62b-3da6ef951f53 and " \
                       "I am from Bugatti manufacturer. " \
            f"My price is 1.0 while I ran for about 1.0."
        self.assertIsInstance(self.car1.__str__(), str)
        self.assertEqual(self.car1.__str__(), expected_res)

    def test_str_failure(self):
        expected_res = "Hi. My name is Coupe 65c11813-3eb5-4d48-b62b-3da6ef951f53 and I am from Bugatti manufacturer. " \
            f"My price is 1.0 while I ran for about 1.0."
        self.assertIsInstance(self.car1.__str__(), str)
        self.assertFalse(self.car1.__str__() == expected_res)


class GarageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.conv_values = [21322, 123123.1231212, "12312"]

        self.conv_failure = [["item_one", "item_two"], ("item_one", "item_two",),
                               {"item_one": "value_one", "item_two": "value_two"},
                               [], (), {}, True, False, None] #changing None position somehow fails the test

        self.car1 = hw.Car(price=1, type="Coupe", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=1)

        self.car2 = hw.Car(price=1, type="Coupe", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=1)

        self.car3 = hw.Car(price=103, type="Coupe", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=1)

        self.car4 = hw.Car(price=1, type="Coupe", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=21)

        self.garage1 = hw.Garage('Amsterdam', self.car1, places=5, owner='be23adf5-3d7f-43f1-9874-e60d61c84523')

        self.garage2 = hw.Garage('Prague', self.car3, places=5, owner='be23adf5-3d7f-43f1-9874-e60d61c84523')

        self.garage3 = hw.Garage(places=5, owner='be23adf5-3d7f-43f1-9874-e60d61c84523', town='Rome')

        self.garage4 = hw.Garage(places=0, owner='be23adf5-3d7f-43f1-9874-e60d61c84523', town='Rome')

        self.uuid_bad_number = 'c4595999-28b9-4a98-bd85-9d59ada33ef'

        self.change_owner_number = [None, 'c4595999-28b9-4a98-bd85-9d59ada33efe']

        self.new_number = str(uuid.uuid4())

        self.bad_uuid_1 = ['1324812871-alfwewqwq-qweqweqww', '#123751-sd63h-13241-sd623h-d27324323hj',
                           '45t45645g45g-464g4g56-4564g54-4564ererre', '', 'fake']

        self.bad_uuid_2 = [["item_one", "item_two"], ("item_one", "item_two",),
                             {"item_one": "value_one", "item_two": "value_two"},
                             [], (), {}, uuid.uuid4(), 21322, 123123.1231212, "12312", True, False]

        self.bad_uuid_3 = [None]

        self.wrong_towns = ['Beijing', 'Brovary', 'Tristram',
                            ["item_one", "item_two"], ("item_one", "item_two",),
                            {"item_one": "value_one", "item_two": "value_two"},
                            [], (), {}, True, False, None]

    def tearDown(self) -> None:
        self.car1 = hw.Car(price=1, type="Coupe", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=1)

        self.car2 = hw.Car(price=1, type="Van", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=1)

        self.car3 = hw.Car(price=103, type="Coupe", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=1)

        self.car4 = hw.Car(price=1, type="Coupe", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=21)

        self.garage1 = hw.Garage('Amsterdam', self.car1, places=5, owner='be23adf5-3d7f-43f1-9874-e60d61c84523')

        self.garage2 = hw.Garage('Prague', self.car3, places=5, owner='be23adf5-3d7f-43f1-9874-e60d61c84523')

        self.garage3 = hw.Garage(places=5, owner='be23adf5-3d7f-43f1-9874-e60d61c84523', town='Rome')

        self.garage4 = hw.Garage(places=0, owner='be23adf5-3d7f-43f1-9874-e60d61c84523', town='Rome')

    def test_to_convert_to_int_success(self):
        for value in self.conv_values:
            self.assertIsInstance(hw.Garage._convert_to_int(value), int)
            self.assertEqual(hw.Garage._convert_to_int(value), int(value))

    def test_to_convert_to_int_failure(self):
        for value in self.conv_failure:
            self.assertEqual(hw.Garage._convert_to_int(value), None)

    def test_owner_check_success(self):
        self.assertEqual(hw.Garage.owner_check(self.change_owner_number[0]), None)
        self.assertEqual(hw.Garage.owner_check(self.change_owner_number[1]), self.change_owner_number[1])

    def test_owner_check_failure(self):
        for value in self.conv_failure[:-1]:
            expected_res = 'You failed! Try again with a string.'
            self.assertEqual(hw.Garage.owner_check(value), expected_res)
        expected_res_2 = 'Failed again! Google how uuid should look like.'
        self.assertEqual(hw.Garage.owner_check(self.uuid_bad_number), expected_res_2)

    def test_town_check_success(self):
        for town in TOWNS:
            self.assertEqual(hw.Garage.town_check(town), town)

    def test_town_check_failure(self):
        for town in self.wrong_towns:
            with self.assertRaises(ValueError) as context:
                hw.Garage.town_check(town)
            self.assertTrue(("Town should be instance of TOWNS! "
                             "Treat yourself with a bit of geography") in context.exception.args)

    def test_add_car_success(self):
        self.assertTrue(self.garage1.free_places() > 0)
        expected_res = "Car has been added."
        self.assertEqual(self.garage1.add_car(self.car2), expected_res)

    def test_add_car_failure(self):
        with self.assertRaises(ValueError) as context:
            self.garage4.add_car(self.car1)
        expected_res = "No free space left!"
        self.assertTrue(expected_res in context.exception.args)

    def test_remove_car_success(self):
        expected_res = "You just deleted that car."
        self.assertEqual(self.garage1.remove_car(self.car1), expected_res)
        self.assertEqual(self.garage2.remove_car(self.car3), expected_res)

    def test_remove_car_failure(self):
        expected_res = "No such car."
        self.assertEqual(self.garage3.remove_car(self.car4), expected_res)

    def test_hit_hat_success(self):
        self.assertEqual(self.garage1.hit_hat(), 1.0)

    def test_free_places_success(self):
        self.assertEqual(self.garage1.free_places(), 4)
        self.assertEqual(self.garage4.free_places(), 0)

    def test_str_success(self):
        expected_res = "Hello. I`m a garage in Amsterdam and I have 5 cars inside me. " \
                         "They are: [Car(1.0, 'Coupe', 'Bugatti', 65c11813-3eb5-4d48-b62b-3da6ef951f53, 1.0)]. " \
                         "All of this is owned by be23adf5-3d7f-43f1-9874-e60d61c84523."
        self.assertEqual(self.garage1.__str__(), expected_res)

    def test_str_failure(self):
        expected_res = "Hello. I`m a garage in Monaco and I have 67 cars inside me. " \
                         "They are: [Car(2.0, 'Coupe', 'Bugatti', 65c11813-3eb5-4d48-b62b-3da6ef951f53, 1.0)]. " \
                         "All of this is owned by eb23adf5-3d7f-43f1-9874-e60d61c84523."
        self.assertFalse(self.garage1.__str__() == expected_res)

    def test_rep_success(self):
        expected_res = "Garages('Amsterdam', '[Car(1.0, 'Coupe', 'Bugatti', " \
                       "65c11813-3eb5-4d48-b62b-3da6ef951f53, 1.0)]', " \
                       "5, be23adf5-3d7f-43f1-9874-e60d61c84523)"
        self.assertEqual(self.garage1.__repr__(), expected_res)

    def test_rep_fail(self):
        expected_res = "Garages('Amsterdam', '[Car(2.0, 'Coupe', 'Bugatti', " \
                       "65d11813-3eb5-4d48-b62b-3da6ef951f53, 1.0)]', 5, be23adf5-3d7f-43f1-9874-e60d61c84523)"
        self.assertFalse(self.garage1.__repr__() == expected_res)


class CesarTest(unittest.TestCase):
    def setUp(self) -> None:
        self.fake_values = [["item_one", "item_two"], ("item_one", "item_two",),
                          {"item_one": "value_one", "item_two": "value_two"},
                          [], (), {}, True, False, None]

        self.car1 = hw.Car(price=1, type="Coupe", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=1)

        self.car2 = hw.Car(price=1, type="Coupe", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=1)

        self.car3 = hw.Car(price=103, type="Coupe", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=1)

        self.car4 = hw.Car(price=1, type="Coupe", producer="Bugatti", number='65c11813-3eb5-4d48-b62b-3da6ef951f53',
                           mileage=21)

        self.garage1 = hw.Garage('Amsterdam', self.car1, places=5, owner='be23adf5-3d7f-43f1-9874-e60d61c84523')

        self.garage2 = hw.Garage('Prague', self.car3, places=5, owner='be23adf5-3d7f-43f1-9874-e60d61c84523')

        self.garage3 = hw.Garage(places=5, owner='be23adf5-3d7f-43f1-9874-e60d61c84523', town='Rome')

        self.garage4 = hw.Garage(places=0, owner='be23adf5-3d7f-43f1-9874-e60d61c84523', town='Rome')

        self.cesar1 = hw.Cesar("Frank", self.garage1, self.garage2, self.garage3, register_id=None)
        self.cesar2 = hw.Cesar("Bob", self.garage4, register_id=None)
        self.cesar3 = hw.Cesar("Lillith", register_id='75c11813-3eb5-4d48-b62b-3da6ef951f57')

    def test_garages_check_success(self):
        self.assertEqual(self.cesar3.garages_check(self.cesar3.garages), [])
        self.assertEqual(self.cesar2.garages_check(self.cesar2.garages),
                         [self.garage4])
        self.assertEqual(self.cesar1.garages_check(self.cesar1.garages),
                         [self.garage1, self.garage2, self.garage3])

    def test_garages_check_failure(self):
        expected_res = 'It should be a Garage, not list, tuple, set, dict, int or float'
        for value in self.fake_values[0:3]:
            with self.assertRaises(AttributeError) as context:
                self.cesar1.garages_check(value)
            self.assertTrue(expected_res in context.exception.args)
        for value_2 in self.fake_values[3:6]:
            self.assertEqual(self.cesar1.garages_check(value_2), [])
        expected_res_2 = "Value should be bool or None"
        for value_3 in self.fake_values[6:]:
            with self.assertRaises(TypeError) as context:
                self.cesar1.garages_check(value_3)
            self.assertTrue(expected_res_2 in context.exception.args)

    def test_garage_count_success(self):
        self.assertEqual(self.cesar1.garage_count(), 3)
        self.assertEqual(self.cesar2.garage_count(), 1)
        self.assertEqual(self.cesar3.garage_count(), None)

    def test_hit_hat_success(self):
        self.assertEqual(self.cesar1.total_hit_hat(), 104.0)
        self.assertEqual(self.cesar2.total_hit_hat(), 0)
        self.assertEqual(self.cesar3.total_hit_hat(), 0)

    def test_cars_count_success(self):
        self.assertEqual(self.cesar1.cars_count(), 2.0)
        self.assertEqual(self.cesar2.cars_count(), 0)
        self.assertEqual(self.cesar3.cars_count(), 0)

    def test_max_free_spaces_success(self):
        self.assertEqual(self.cesar1.max_free_spaces(), {34: 5})
        self.assertEqual(self.cesar2.max_free_spaces(), "No free spaces left in the garages. "
                                                        "Hope you`re proud of yourself")
        self.assertEqual(self.cesar3.max_free_spaces(), "Seems like there are no garages belonging to you")

    def test_max_free_spaces_failure(self):
        self.assertFalse(self.cesar1.max_free_spaces() == {2: 15})
        self.assertFalse(self.cesar1.max_free_spaces() == "No free spaces left in the garages. "
                                                          "Hope you`re proud of yourself")
        self.assertFalse(self.cesar2.max_free_spaces() == "Seems like there are no garages belonging to you")

    def test_add_car_success(self):
        self.assertEqual(self.cesar1.add_car(self.car1), "Car has been added to garage 6")
        self.assertEqual(self.cesar1.add_car(self.car2, self.garage1), "Car has been added to garage 4")

    def test_add_car_failure(self):
        for value in self.fake_values:
            for value_2 in self.fake_values:
                with self.assertRaises(AttributeError) as context:
                    self.cesar1.add_car(value, value_2)
                self.assertFalse(
                    "Car should be instance of Car and garage should be instance of Garage" in context.exception.args)
        self.assertEqual(self.cesar1.add_car(self.car1, self.garage4), "Get out of here! "
                                                                       "You just came to wrong garage, son!")
        self.assertEqual(self.cesar3.add_car(self.car1), "Seems like there are no garages belonging to you")
        self.assertEqual(self.cesar2.add_car(self.car1), "No free spaces left in the garages. "
                                                         "Hope you`re proud of yourself")
        self.assertEqual(self.cesar2.add_car(self.car2, self.garage4), "No free spaces in the garage 3")

    def test_str_success(self):
        expected_res_1 = "Hello. I`m a philanthropist, billionaire Lillith and my ID is " \
                         "75c11813-3eb5-4d48-b62b-3da6ef951f57. I`m a proud owner of this cuties: []."
        self.assertEqual(self.cesar3.__str__(), expected_res_1)
        uuid = self.cesar1.register_id
        expected_res_2 = f"""Hello. I`m a philanthropist, billionaire Frank and my ID is {uuid}. I`m a proud owner of this cuties: [Garages('Amsterdam', '[Car(1.0, 'Coupe', 'Bugatti', 65c11813-3eb5-4d48-b62b-3da6ef951f53, 1.0)]', 5, be23adf5-3d7f-43f1-9874-e60d61c84523), Garages('Prague', '[Car(103.0, 'Coupe', 'Bugatti', 65c11813-3eb5-4d48-b62b-3da6ef951f53, 1.0)]', 5, be23adf5-3d7f-43f1-9874-e60d61c84523), Garages('Rome', '[]', 5, be23adf5-3d7f-43f1-9874-e60d61c84523)]."""
        self.assertEqual(self.cesar1.__str__(), expected_res_2)

    def test_str_failure(self):
        expected_res_1 = "Hello. I`m a philanthropist, billionaire Fillith and my ID is " \
                         "75c11813-3eb5-4d48-b62b-3da6ef951f57. I`m a proud owner of this cuties: []."
        self.assertFalse(self.cesar3.__str__() == expected_res_1)

    def test_repr_success(self):
        expected_res_ces_3 = "Cesar('Lillith', 75c11813-3eb5-4d48-b62b-3da6ef951f57, '[]')"
        self.assertEqual(self.cesar3.__repr__(), expected_res_ces_3)
        register_id = self.cesar2.register_id
        expected_res_ces_2 = f"""Cesar('Bob', {register_id}, '[Garages('Rome', '[]', 0, be23adf5-3d7f-43f1-9874-e60d61c84523)]')"""
        self.assertEqual(self.cesar2.__repr__(), expected_res_ces_2)

    def test_repr_failure(self):
        expected_res_ces_3 = "Cesar('Fillith', 75c11813-3eb5-4d48-b62b-3da6ef951f57, '[]')"
        self.assertFalse(self.cesar3.__repr__() == expected_res_ces_3)
        register_id = self.cesar2.register_id
        expected_res_ces_2 = f"""Cesar('Wob_wob', {register_id}, '[Garages('Rome', '[]', 0, be23adf5-3d7f-43f1-9874-e60d61c84523)]')"""
        self.assertFalse(self.cesar2.__repr__() == expected_res_ces_2)