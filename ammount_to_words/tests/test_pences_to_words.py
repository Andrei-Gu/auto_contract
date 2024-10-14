import unittest
from ..main import pences_to_words


class TestPencesToWords(unittest.TestCase):
    def test_for_1(self):
        self.assertEqual(pences_to_words(1), '01 копейка')

    def test_for_23(self):
        self.assertEqual(pences_to_words(23), '23 копейки')

    def test_for_14(self):
        self.assertEqual(pences_to_words(14), '14 копеек')

    def test_for_77(self):
        self.assertEqual(pences_to_words(77), '77 копеек')


if __name__ == '__main__':
    unittest.main()
