import unittest
from ..main import pences_to_string


class TestPencesToString(unittest.TestCase):
    def test_with_zero(self):
        self.assertEqual(pences_to_string(3), '03')

    def test_without_zero(self):
        self.assertEqual(pences_to_string(51), '51')


if __name__ == '__main__':
    unittest.main()
