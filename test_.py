import unittest
import multiples_factors

class _test_(unittest.TestCase):
    """A test class for the v2math module."""

    def setUp(self):
        """Setting up."""
        self.num = multiples_factors.get_factors(6)
        self.r = multiples_factors.get_multiples(6, 4)
        self.f = multiples_factors.check_factor(6, 4)
        self.m = multiples_factors.check_multiple(4, 8)
        self.l = multiples_factors.is_prime(5)

    def test_get_factors(self):
        """Test get_factors()."""
        self.assertEqual(self.num, [1, 2, 3, 6])
    
    def test_get_multiples(self):
        """Test get_multiples()."""
        self.assertEqual(self.r, [6, 12, 18, 24])

    def test_check_factor(self):
        """Test check_factor."""
        self.assertFalse(self.f)

    def test_check_multiple(self):
        self.assertTrue(self.m)

    def test_is_prime(self):
        """Tests is_prime()."""
        self.assertTrue(self.l)

if __name__ == '__main__':
    unittest.main()