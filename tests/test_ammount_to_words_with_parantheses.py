import unittest
from ..main import ammount_to_words_with_parentheses


class TestAmmountToWordsWithParentheses(unittest.TestCase):
    def test_ammount_to_words_with_parentheses_0_005(self):
        self.assertEqual(ammount_to_words_with_parentheses('0.005'), '(ноль) рублей 01 копейка')


    def test_ammount_to_words_with_parentheses_6_871(self):
        self.assertEqual(ammount_to_words_with_parentheses('6.871'), '(шесть) рублей 87 копеек')


    def test_ammount_to_words_with_parentheses_202(self):
        self.assertEqual(ammount_to_words_with_parentheses('202'), '(двести два) рубля 00 копеек')


    def test_ammount_to_words_with_parentheses_700_841(self):
        self.assertEqual(ammount_to_words_with_parentheses('700_841'), '(семьсот тысяч восемьсот сорок один) рубль 00 копеек')


    def test_ammount_to_words_with_parentheses_92_601_015_23(self):
        self.assertEqual(ammount_to_words_with_parentheses('92 601 015.23'), '(девяноста два миллиона шестьсот одна тысяча пятнадцать) рублей 23 копейки')


    def test_ammount_to_words_with_parentheses_(self):
        self.assertEqual(ammount_to_words_with_parentheses('43 000 000 052'), '(сорок три миллиарда пятьдесят два) рубля 00 копеек')


if __name__ == '__main__':
    unittest.main()
