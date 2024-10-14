import unittest
from ..main import exceeding_limits


class TestExceedingLimits(unittest.TestCase):
    def test_less_than_limit(self):
        self.assertTrue(exceeding_limits(-10))

    def test_bigger_than_limit(self):
        self.assertTrue(exceeding_limits(25_999_888_777_555))

    def test_within_acceptable_limits(self):
        self.assertFalse(exceeding_limits(77555))


if __name__ == '__main__':
    unittest.main()
