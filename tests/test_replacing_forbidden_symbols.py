import unittest
from ..main import replacing_forbidden_symbols


class TestReplacingForbiddenSymbols(unittest.TestCase):
    def test_replacing_question_mark(self):
        self.assertEqual(replacing_forbidden_symbols('?some ?text? for? test? ???'), 'some text for test ')


    def test_replacing_colon(self):
        self.assertEqual(replacing_forbidden_symbols(':some :text: for: test: :::'), 'some text for test ')


    def test_replacing_slash(self):
        self.assertEqual(replacing_forbidden_symbols('/some /text/ for/ test/ ///'), 'some text for test ')


    def test_replacing_asterisk(self):
        self.assertEqual(replacing_forbidden_symbols('*some *text* for* test* ***'), 'some text for test ')


    def test_replacing_quotation_mark(self):
        self.assertEqual(replacing_forbidden_symbols('"some "text" for" test" """'), 'some text for test ')


    def test_replacing_less_than_sign(self):
        self.assertEqual(replacing_forbidden_symbols('<some <text< for< test< <<<'), 'some text for test ')


    def test_replacing_greater_than_sign(self):
        self.assertEqual(replacing_forbidden_symbols('>some >text> for> test> >>>'), 'some text for test ')


    def test_replacing_pipe(self):
        self.assertEqual(replacing_forbidden_symbols('|some |text| for| test| |||'), 'some text for test ')


    def test_replacing_backslash(self):
        self.assertEqual(replacing_forbidden_symbols('some text\ for\ test\ '), 'some text for test ')


if __name__ == '__main__':
    unittest.main()
