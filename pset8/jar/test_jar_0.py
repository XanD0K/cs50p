import unittest

from jar import Jar


class TestJar(unittest.TestCase):
    def test_init(self):
        jar = Jar()
        assert jar.capacity == 12
        assert jar.size == 0
        jar = Jar(5)
        assert jar.capacity == 5
        assert jar.size == 0
        with self.assertRaises(ValueError):
            Jar(-1)
        jar = Jar()
        with self.assertRaises(AttributeError):
            jar.capacity = 20

    def test_str(self):
        jar = Jar()
        assert str(jar) == ""
        jar.deposit(1)
        assert str(jar) == "🍪"
        jar.deposit(11)
        assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    def test_deposit(self):
        jar = Jar()
        assert jar.deposit(5) == None
        assert jar.size == 5
        assert str(jar) == "🍪🍪🍪🍪🍪"
        with self.assertRaises(ValueError):
            jar.deposit(-1)
        with self.assertRaises(ValueError):
            jar.deposit(10)

    def test_withdraw(self):
        jar = Jar()
        jar.deposit(10)
        assert jar.size == 10
        assert jar.withdraw(3) == None
        assert jar.size == 7
        assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"
        assert jar.withdraw(5) == None
        assert jar.size == 2
        assert str(jar) == "🍪🍪"
        with self.assertRaises(ValueError):
            jar.withdraw(-1)
        with self.assertRaises(ValueError):
            jar.withdraw(5)