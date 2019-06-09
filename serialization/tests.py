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
            with self.assertRaises(ValueError, msg="Type should be an instance of CAR_TYPES! Please, reconsider.") as context:
                hw.Car.type_checking(type)
            self.assertTrue("Type should be an instance of CAR_TYPES! Please, reconsider." in context.exception.args)

    def test_car_producer_checking_success(self):
        for producer in CARS_PRODUCER:
            self.assertEqual(hw.Car.producer_checking(producer), producer)

    def test_car_producer_checking_failure(self):
        for producer in self.fake_producers:
            with self.assertRaises(ValueError, msg="Producer should be an instance of CARS_PRODUCER! When will you learn?") as context:
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
        expected_res = "Hello. My name is Coupe 65c11813-3eb5-4d48-b62b-3da6ef951f53 and I am from Bugatti manufacturer. " \
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
            self.assertTrue(("Town should be instance of TOWNS! Treat yourself with a bit of geography") in context.exception.args)

    def test_add_car_success(self):
        self.assertTrue(self.garage1.free_place() > 0)
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
        self.assertEqual(self.garage1.free_place(), 4)
        self.assertEqual(self.garage4.free_place(), 0)

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
        expected_res = "Garages('Amsterdam', '[Car(1.0, 'Coupe', 'Bugatti', 65c11813-3eb5-4d48-b62b-3da6ef951f53, 1.0)]', " \
                       "5, be23adf5-3d7f-43f1-9874-e60d61c84523)"
        self.assertEqual(self.garage1.__repr__(), expected_res)

    def test_rep_fail(self):
        expected_res = "Garages('Amsterdam', '[Car(2.0, 'Coupe', 'Bugatti', " \
                       "65d11813-3eb5-4d48-b62b-3da6ef951f53, 1.0)]', 5, be23adf5-3d7f-43f1-9874-e60d61c84523)"
        self.assertFalse(self.garage1.__repr__() == expected_res)