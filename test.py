import unittest
from hello import say_hello_to

class HelloTest(unittest.TestCase):

    def test_hello(self):
        say_hello_to('Marc')


if __name__ == '__main__':
    unittest.main()
