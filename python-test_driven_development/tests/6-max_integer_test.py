#!/usr/bin/python3
"""Unittests for the max_integer function."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_regular_list(self):
        """Test with a normal list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test when the max is the first element."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test when the max is in the middle."""
        self.assertEqual(max_integer([1, 5, 2, 3]), 5)

    def test_single_element(self):
        """Test with a single element list."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Test with no argument uses default empty list."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Test with all negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_negative_positive(self):
        """Test with both negative and positive numbers."""
        self.assertEqual(max_integer([-1, 0, 3, -5]), 3)

    def test_duplicate_values(self):
        """Test with duplicate values."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_max_is_zero(self):
        """Test when the max value is zero."""
        self.assertEqual(max_integer([-1, -2, 0]), 0)

    def test_floats(self):
        """Test with float values."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_int_float(self):
        """Test with mixed integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)


if __name__ == "__main__":
    unittest.main()
