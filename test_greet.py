import unittest

from greet import greet, shout


class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("world"), "Hello, world!")

    def test_shout(self):
        self.assertEqual(shout("this is a practice project"), "THIS IS A PRACTICE PROJECT!")


if __name__ == "__main__":
    unittest.main()
