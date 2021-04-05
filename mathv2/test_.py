import unittest
import multiples_factors

class TestV2Math(unittest.TestCase):
    """A test class for the v2math module."""

    def setUp(self):
        """Initialize attributes for setting up."""
        self.factors = multiples_factors.get_factors(6)
        self.multiples = multiples_factors.get_multiples(6, 4)
        self.factor = multiples_factors.check_factor(6, 4)
        self.multiple = multiples_factors.check_multiple(4, 8)
        self.prime = multiples_factors.is_prime(5)
        self.common_factors = multiples_factors.get_common_factors(10, 12)

    def test_get_factors(self):
        """Test get_factors()."""
        self.assertEqual(self.factors, [1, 2, 3, 6])
    
    def test_get_multiples(self):
        """Test get_multiples()."""
        self.assertEqual(self.multiples, [6, 12, 18, 24])

    def test_check_factor(self):
        """Test check_factor."""
        self.assertFalse(self.factor)

    def test_check_multiple(self):
        self.assertTrue(self.multiple)

    def test_is_prime(self):
        """Tests is_prime()."""
        self.assertTrue(self.prime)

    def test_get_common_factors(self):
        """Test get_common_factors()"""
        self.assertEqual(self.common_factors, [1, 2])

if __name__ == '__main__':
    unittest.main()