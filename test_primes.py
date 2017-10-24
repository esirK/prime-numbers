import unittest
from primes import isPrime


class TestPrimes(unittest.TestCase):
    def test_num_is_prime(self):
        # numbers
        numbers = [2, 5, 7, 11]
        for number in numbers:
            self.assertTrue(isPrime(number))

    def test_num_not_prime(self):
        numbers = [1, -5, 6, 8]
        for number in numbers:
            self.assertFalse(isPrime(number))


if __name__ == "__main__":
    unittest.main()
