import unittest, random
from ..main import getting_declension


class TestGettingDeclension(unittest.TestCase):
    def setUp(self):
        self.declensions = ('рубль', 'рубля', 'рублей')
        self.tuple_for_0_dcln = (1, 21, 71)
        self.tuple_for_1_dcln = (2, 3, 4, 22, 53, 84)
        self.tuple_for_2_dcln_1 = (0, 11, 12, 13, 14)
        self.tuple_for_2_dcln_2 = (7, 16, 25, 77, 98)

    def test_for_0_dcln(self):
        self.assertEqual(getting_declension(random.choice(self.tuple_for_0_dcln),
                                            self.declensions),
                         self.declensions[0],
                         )

    def test_for_1_dcln(self):
        self.assertEqual(getting_declension(random.choice(self.tuple_for_1_dcln),
                                            self.declensions),
                         self.declensions[1],
                         )

    def test_for_2_dcln_1(self):
        self.assertEqual(getting_declension(random.choice(self.tuple_for_2_dcln_1),
                                            self.declensions),
                         self.declensions[2],
                         )

    def test_for_2_dcln_2(self):
        self.assertEqual(getting_declension(random.choice(self.tuple_for_2_dcln_2),
                                            self.declensions),
                         self.declensions[2],
                         )


if __name__ == '__main__':
    unittest.main()
