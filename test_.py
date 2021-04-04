import unittest
from multiples_factors import get_factors

class _test_(unittest.TestCase):
    """A test class for the v2math module."""

    def setUp(self):
        """Setting up."""
        self.num = get_factors(6)

    def test_get_factors(self):
        """Test get_factors()."""
        self.assertEqual(self.num, [1, 2, 3, 6])

if __name__ == '__main__':
    unittest.main()