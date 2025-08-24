# Used asserEqual to check equalitty


import unittest

from jar import Jar


class TestJar(unittest.TestCase):
    def test_init_default_capacity(self):
        jar = Jar()
        self.assertEqual(jar.capacity, 12)
        self.assertEqual(jar.size, 0)

    def test_str_empty(self):
        jar = Jar()
        self.assertEqual(str(jar), "")

    def test_deposit_valid(self):
        jar = Jar()
        jar.deposit(5)
        self.assertEqual(jar.size, 5)
        self.assertEqual(str(jar), "🍪" * 5)

    def test_deposit_negative(self):
        jar = Jar()
        with self.assertRaises(ValueError):
            jar.deposit(-1)

    def test_deposit_over_capacity(self):
        jar = Jar()
        jar.deposit(10)
        with self.assertRaises(ValueError):
            jar.deposit(3)

    def test_withdraw_valid(self):
        jar = Jar()
        jar.deposit(5)
        jar.withdraw(2)
        self.assertEqual(jar.size, 3)

    def test_withdraw_negative(self):
        jar = Jar()
        with self.assertRaises(ValueError):
            jar.withdraw(-1)

    def test_withdraw_too_many(self):
        jar = Jar()
        jar.deposit(2)
        with self.assertRaises(ValueError):
            jar.withdraw(3)

    def test_capacity_read_only(self):
        jar = Jar()
        with self.assertRaises(AttributeError):
            jar.capacity = 20

    def test_size_read_only(self):
        jar = Jar()
        with self.assertRaises(AttributeError):
            jar.size = 5

if __name__ == "__main__":
    unittest.main()