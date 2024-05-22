import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([3]), 3)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_all_same_elements(self):
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_floats_and_integers(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 2]), 3.5)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 1000000]), 1000000)

    def test_list_with_zero(self):
        self.assertEqual(max_integer([0, -1, -2, -3]), 0)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)


if __name__ == '__main__':
    unittest.main()
