import unittest
from klickbrick.klickbrick import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello("Mark"), "Hello Mark!")


if __name__ == "__main__":
    unittest.main()
