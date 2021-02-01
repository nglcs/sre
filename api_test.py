from api import default
import unittest

class TestApp(unittest.TestCase):
    def test_return_backwards_string(self):

        self.assertEqual("It`s Work!", default())

if __name__ == "__main__":
    unittest.main()
