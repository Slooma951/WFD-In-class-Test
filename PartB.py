import unittest
from PartA import Phone, Smartphone

class TestPhone(unittest.TestCase):

    def setUp(self):
        self.phone = Phone("iPhone", "13", 2021, 799, "Midnight Black")
        self.smartphone = Smartphone("Iphone", "15", 2023, 899, "green", "IOS17", 256)

    def test_instance_of_class(self):  #B2
        self.assertIsInstance(self.phone, Phone)
        self.assertIsInstance(self.smartphone, Smartphone)

    def test_not_instance_of_class(self):  # B3
        self.assertNotIsInstance(self.phone, int)
        self.assertNotIsInstance(self.smartphone, int)

    def test_objects_identical(self):  #B4
        phone2 = self.phone
        self.assertIs(self.phone, phone2)

    def test_update_methods(self):  #B5
        self.phone.update_price(600)
        self.phone.update_colour("Pink")
        self.assertEqual(self.phone.price, 600)
        self.assertEqual(self.phone.colour, "Pink")

        self.smartphone.update_os("IOS18")
        self.smartphone.update_storage(512)
        self.assertEqual(self.smartphone.os, "IOS18")
        self.assertEqual(self.smartphone.storage, 512)

if __name__ == "__main__":  #B6
    unittest.main()
