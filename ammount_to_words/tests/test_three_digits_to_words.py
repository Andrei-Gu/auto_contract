import unittest
from ..main import three_digits_to_words


class TestThreeDigitsToWords(unittest.TestCase):
    def test_for_1_female(self):
        self.assertEqual(three_digits_to_words(1, 1), 'одна')

    def test_for_2_female(self):
        self.assertEqual(three_digits_to_words(2, 1), 'две')

    def test_for_1_male(self):
        self.assertEqual(three_digits_to_words(1, 2), 'один')

    def test_for_2_male(self):
        self.assertEqual(three_digits_to_words(2, 2), 'два')

    def test_for_3(self):
        self.assertEqual(three_digits_to_words(3, 2), 'три')

    def test_for_10(self):
        self.assertEqual(three_digits_to_words(10, 2), 'десять')

    def test_for_19(self):
        self.assertEqual(three_digits_to_words(19, 2), 'девятнадцать')

    def test_for_20(self):
        self.assertEqual(three_digits_to_words(20, 1), 'двадцать')

    def test_for_31_female(self):
        self.assertEqual(three_digits_to_words(31, 1), 'тридцать одна')

    def test_for_32_female(self):
        self.assertEqual(three_digits_to_words(32, 1), 'тридцать две')

    def test_for_31_male(self):
        self.assertEqual(three_digits_to_words(31, 2), 'тридцать один')

    def test_for_32_male(self):
        self.assertEqual(three_digits_to_words(32, 2), 'тридцать два')

    def test_for_33(self):
        self.assertEqual(three_digits_to_words(33, 1), 'тридцать три')

    def test_for_47(self):
        self.assertEqual(three_digits_to_words(47, 1), 'сорок семь')

    def test_for_99(self):
        self.assertEqual(three_digits_to_words(99, 1), 'девяноста девять')

    def test_for_100(self):
        self.assertEqual(three_digits_to_words(100, 1), 'сто')

    def test_for_900(self):
        self.assertEqual(three_digits_to_words(900, 1), 'девятьсот')

    def test_for_940(self):
        self.assertEqual(three_digits_to_words(940, 1), 'девятьсот сорок')

    def test_for_999(self):
        self.assertEqual(three_digits_to_words(999, 1), 'девятьсот девяноста девять')

    def test_for_101_female(self):
        self.assertEqual(three_digits_to_words(101, 1), 'сто одна')

    def test_for_102_female(self):
        self.assertEqual(three_digits_to_words(102, 1), 'сто две')

    def test_for_101_male(self):
        self.assertEqual(three_digits_to_words(101, 2), 'сто один')

    def test_for_102_male(self):
        self.assertEqual(three_digits_to_words(102, 2), 'сто два')

    def test_for_103(self):
        self.assertEqual(three_digits_to_words(103, 2), 'сто три')

    def test_for_215(self):
        self.assertEqual(three_digits_to_words(215, 2), 'двести пятнадцать')

    def test_for_275(self):
        self.assertEqual(three_digits_to_words(275, 2), 'двести семьдесят пять')

    def test_for_581_female(self):
        self.assertEqual(three_digits_to_words(581, 1), 'пятьсот восемьдесят одна')

    def test_for_582_female(self):
        self.assertEqual(three_digits_to_words(582, 1), 'пятьсот восемьдесят две')

    def test_for_581_male(self):
        self.assertEqual(three_digits_to_words(581, 2), 'пятьсот восемьдесят один')

    def test_for_582_male(self):
        self.assertEqual(three_digits_to_words(582, 2), 'пятьсот восемьдесят два')

    def test_for_698(self):
        self.assertEqual(three_digits_to_words(698, 1), 'шестьсот девяноста восемь')


if __name__ == '__main__':
    unittest.main()
