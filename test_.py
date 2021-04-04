import unittest
import multiples_factors

class _test_(unittest.TestCase):
    """A test class for the v2math module."""

    def setUp(self):
        """Setting up."""
        self.num = multiples_factors.get_factors(6)
        self.r = multiples_factors.get_multiples(6, 4)

    def test_get_factors(self):
        """Test get_factors()."""
        self.assertEqual(self.num, [1, 2, 3, 6])
    
    def test_get_multiples(self):
        """Test get_multiples()."""
        self.assertEqual(self.r, [6, 12, 18, 24])

if __name__ == '__main__':
    unittest.main()