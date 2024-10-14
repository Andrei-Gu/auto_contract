import unittest
from ..main import main


class TestMainWithInvalidValues(unittest.TestCase):
    def setUp(self):
        self.invalid_values = ('1,5.',
                               '1.5,',
                               '1.5.',
                               '1,5,',
                               '.1,5',
                               ',1.5',
                               '1-5',
                               ',.15',
                               '.,15',
                               ',,15',
                               '..15',
                               '--15',
                               '++15',
                               '98 ,.',
                               '98_.,',
                               '98,,15',
                               '98..15',
                               '98--',
                               '(15)',
                               '(15)98',
                               '15(98)',
                               ')15(',
                               ')15',
                               '15(',
                               'abc',
                               'ABC',
                               'abc 123',
                               '123abc',
                               'ABC 123',
                               '123ABC',
                               'йюф',
                               'ЙЮФ',
                               'йюф 123',
                               '123йюф',
                               'ЙЮФ 123',
                               '123ЙЮФ',
                               '123:0',
                               '!123',
                               '1#2^3',
                               'adc!@#',
                               'йюф!@#',
                               '*()&',
                               '123 *()&',
                               '€46548',
                               '14|65',
                               )

    def test_invalid_values(self):
        for value in self.invalid_values:
            self.assertEqual(main(value), 'Введенные данные имеют некорректный формат')


if __name__ == '__main__':
    unittest.main()
