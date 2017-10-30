import unittest
from primes import is_prime


class TestPrimes(unittest.TestCase):
    def test_num_is_prime(self):
        """Test if the function returns True when passed prime numbers"""
        # numbers
        numbers = [2, 5, 7, 11]
        for number in numbers:
            self.assertTrue(is_prime(number))

    def test_num_not_prime(self):
        """Test if the function returns False when passed non prime numbers"""
        numbers = [1, -5, 6, 8, 9.2, 11.1]
        for number in numbers:
            self.assertFalse(is_prime(number))
    def test_string_with_letters(self):
        """Test if invalid values are handled"""
        numbers = ["man", "Andela", "60o", "TIA"]
        for number in numbers:
            self.assertEqual(is_prime(number), "Please enter a valid number")

if __name__ == "__main__":
    unittest.main()
