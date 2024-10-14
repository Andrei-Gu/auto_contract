import unittest
from ..main import two_digits_to_words

class TestTwoDigitsToWords(unittest.TestCase):
    def test_for_1_female(self):
        self.assertEqual(two_digits_to_words(1, 1), ['одна'])

    def test_for_2_female(self):
        self.assertEqual(two_digits_to_words(2, 1), ['две'])

    def test_for_1_male(self):
        self.assertEqual(two_digits_to_words(1, 2), ['один'])

    def test_for_2_male(self):
        self.assertEqual(two_digits_to_words(2, 2), ['два'])

    def test_for_3(self):
        self.assertEqual(two_digits_to_words(3, 2), ['три'])

    def test_for_10(self):
        self.assertEqual(two_digits_to_words(10, 2), ['десять'])

    def test_for_19(self):
        self.assertEqual(two_digits_to_words(19, 2), ['девятнадцать'])

    def test_for_20(self):
        self.assertEqual(two_digits_to_words(20, 1), ['двадцать'])

    def test_for_31_female(self):
        self.assertEqual(two_digits_to_words(31, 1), ['одна', 'тридцать'])

    def test_for_32_female(self):
        self.assertEqual(two_digits_to_words(32, 1), ['две', 'тридцать'])

    def test_for_31_male(self):
        self.assertEqual(two_digits_to_words(31, 2), ['один', 'тридцать'])

    def test_for_32_male(self):
        self.assertEqual(two_digits_to_words(32, 2), ['два', 'тридцать'])

    def test_for_33(self):
        self.assertEqual(two_digits_to_words(33, 1), ['три', 'тридцать'])

    def test_for_47(self):
        self.assertEqual(two_digits_to_words(47, 1), ['семь', 'сорок'])

    def test_for_99(self):
        self.assertEqual(two_digits_to_words(99, 1), ['девять', 'девяноста'])


if __name__ == '__main__':
    unittest.main()
