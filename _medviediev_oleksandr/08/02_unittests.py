import unittest
from code_to_test import multiply


class TestClass(unittest.TestCase):

    def test_multiply(self):

        result = multiply(2, 2)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
