import unittest
from main import Hello

class MyTestCase(unittest.TestCase):
    def test_hello(self):
        hello = Hello()
        self.assertEqual(hello.message, 'Hello world!')

if __name__ == '__main__':
    print("Test Cases")
    unittest.main()