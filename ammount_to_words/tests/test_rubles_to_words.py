import unittest
from ..main import rubles_to_words


class TestRublesToWords(unittest.TestCase):
    def test_for_0(self):
        self.assertEqual(rubles_to_words(0), 'ноль рублей')

    def test_for_1(self):
        self.assertEqual(rubles_to_words(1), 'один рубль')

    def test_for_2(self):
        self.assertEqual(rubles_to_words(2), 'два рубля')

    def test_for_3(self):
        self.assertEqual(rubles_to_words(3), 'три рубля')

    def test_for_11(self):
        self.assertEqual(rubles_to_words(11), 'одиннадцать рублей')

    def test_for_18(self):
        self.assertEqual(rubles_to_words(18), 'восемнадцать рублей')

    def test_for_20(self):
        self.assertEqual(rubles_to_words(20), 'двадцать рублей')

    def test_for_31(self):
        self.assertEqual(rubles_to_words(31), 'тридцать один рубль')

    def test_for_32(self):
        self.assertEqual(rubles_to_words(32), 'тридцать два рубля')

    def test_for_33(self):
        self.assertEqual(rubles_to_words(33), 'тридцать три рубля')

    def test_for_47(self):
        self.assertEqual(rubles_to_words(47), 'сорок семь рублей')

    def test_for_99(self):
        self.assertEqual(rubles_to_words(99), 'девяноста девять рублей')

    def test_for_100(self):
        self.assertEqual(rubles_to_words(100), 'сто рублей')

    def test_for_900(self):
        self.assertEqual(rubles_to_words(900), 'девятьсот рублей')

    def test_for_940(self):
        self.assertEqual(rubles_to_words(940), 'девятьсот сорок рублей')

    def test_for_999(self):
        self.assertEqual(rubles_to_words(999), 'девятьсот девяноста девять рублей')

    def test_for_101(self):
        self.assertEqual(rubles_to_words(101), 'сто один рубль')

    def test_for_102(self):
        self.assertEqual(rubles_to_words(102), 'сто два рубля')

    def test_for_103(self):
        self.assertEqual(rubles_to_words(103), 'сто три рубля')

    def test_for_215(self):
        self.assertEqual(rubles_to_words(215), 'двести пятнадцать рублей')

    def test_for_275(self):
        self.assertEqual(rubles_to_words(275), 'двести семьдесят пять рублей')

    def test_for_581(self):
        self.assertEqual(rubles_to_words(581), 'пятьсот восемьдесят один рубль')

    def test_for_582(self):
        self.assertEqual(rubles_to_words(582), 'пятьсот восемьдесят два рубля')

    def test_for_698(self):
        self.assertEqual(rubles_to_words(698), 'шестьсот девяноста восемь рублей')

    def test_for_1000(self):
        self.assertEqual(rubles_to_words(1000), 'одна тысяча рублей')

    def test_for_2000(self):
        self.assertEqual(rubles_to_words(2000), 'две тысячи рублей')

    def test_for_3000(self):
        self.assertEqual(rubles_to_words(3000), 'три тысячи рублей')

    def test_for_4000(self):
        self.assertEqual(rubles_to_words(4000), 'четыре тысячи рублей')

    def test_for_5000(self):
        self.assertEqual(rubles_to_words(5000), 'пять тысяч рублей')

    def test_for_6001(self):
        self.assertEqual(rubles_to_words(6001), 'шесть тысяч один рубль')

    def test_for_7010(self):
        self.assertEqual(rubles_to_words(7010), 'семь тысяч десять рублей')

    def test_for_8047(self):
        self.assertEqual(rubles_to_words(8047), 'восемь тысяч сорок семь рублей')

    def test_for_9100(self):
        self.assertEqual(rubles_to_words(9100), 'девять тысяч сто рублей')

    def test_for_10101(self):
        self.assertEqual(rubles_to_words(10101), 'десять тысяч сто один рубль')

    def test_for_10101(self):
        self.assertEqual(rubles_to_words(10101), 'десять тысяч сто один рубль')

    def test_for_11205(self):
        self.assertEqual(rubles_to_words(11205), 'одиннадцать тысяч двести пять рублей')

    def test_for_73917(self):
        self.assertEqual(rubles_to_words(73917), 'семьдесят три тысячи девятьсот семнадцать рублей')

    def test_for_81789(self):
        self.assertEqual(rubles_to_words(81789), 'восемьдесят одна тысяча семьсот восемьдесят девять рублей')

    def test_for_99000(self):
        self.assertEqual(rubles_to_words(99000), 'девяноста девять тысяч рублей')

    def test_for_100000(self):
        self.assertEqual(rubles_to_words(100000), 'сто тысяч рублей')

    def test_for_200001(self):
        self.assertEqual(rubles_to_words(200001), 'двести тысяч один рубль')

    def test_for_300018(self):
        self.assertEqual(rubles_to_words(300018), 'триста тысяч восемнадцать рублей')

    def test_for_400065(self):
        self.assertEqual(rubles_to_words(400065), 'четыреста тысяч шестьдесят пять рублей')

    def test_for_500_100(self):
        self.assertEqual(rubles_to_words(500_100), 'пятьсот тысяч сто рублей')

    def test_for_600_702(self):
        self.assertEqual(rubles_to_words(600_702), 'шестьсот тысяч семьсот два рубля')

    def test_for_700_841(self):
        self.assertEqual(rubles_to_words(700_841), 'семьсот тысяч восемьсот сорок один рубль')

    def test_for_801_000(self):
        self.assertEqual(rubles_to_words(801_000), 'восемьсот одна тысяча рублей')

    def test_for_802_000(self):
        self.assertEqual(rubles_to_words(802_000), 'восемьсот две тысячи рублей')

    def test_for_805_000(self):
        self.assertEqual(rubles_to_words(805_000), 'восемьсот пять тысяч рублей')

    def test_for_914_000(self):
        self.assertEqual(rubles_to_words(914_000), 'девятьсот четырнадцать тысяч рублей')

    def test_for_993_123(self):
        self.assertEqual(rubles_to_words(993_123), 'девятьсот девяноста три тысячи сто двадцать три рубля')

    def test_for_1_000_000(self):
        self.assertEqual(rubles_to_words(1_000_000), 'один миллион рублей')

    def test_for_2_000_002(self):
        self.assertEqual(rubles_to_words(2_000_002), 'два миллиона два рубля')

    def test_for_3_000_005(self):
        self.assertEqual(rubles_to_words(3_000_005), 'три миллиона пять рублей')

    def test_for_5_000_016(self):
        self.assertEqual(rubles_to_words(5_000_016), 'пять миллионов шестнадцать рублей')

    def test_for_6_000_063(self):
        self.assertEqual(rubles_to_words(6_000_063), 'шесть миллионов шестьдесят три рубля')

    def test_for_63_000_000(self):
        self.assertEqual(rubles_to_words(63_000_000), 'шестьдесят три миллиона рублей')

    def test_for_11_000_300(self):
        self.assertEqual(rubles_to_words(11_000_300), 'одиннадцать миллионов триста рублей')

    def test_for_45_000_501(self):
        self.assertEqual(rubles_to_words(45_000_501), 'сорок пять миллионов пятьсот один рубль')

    def test_for_57_000_732(self):
        self.assertEqual(rubles_to_words(57_000_732), 'пятьдесят семь миллионов семьсот тридцать два рубля')

    def test_for_60_001_000(self):
        self.assertEqual(rubles_to_words(60_001_000), 'шестьдесят миллионов одна тысяча рублей')

    def test_for_74_002_001(self):
        self.assertEqual(rubles_to_words(74_002_001), 'семьдесят четыре миллиона две тысячи один рубль')

    def test_for_77_005_999(self):
        self.assertEqual(rubles_to_words(77_005_999), 'семьдесят семь миллионов пять тысяч девятьсот девяноста девять рублей')

    def test_for_83_013_000(self):
        self.assertEqual(rubles_to_words(83_013_000), 'восемьдесят три миллиона тринадцать тысяч рублей')

    def test_for_84_037_000(self):
        self.assertEqual(rubles_to_words(84_037_000), 'восемьдесят четыре миллиона тридцать семь тысяч рублей')

    def test_for_91_500_007(self):
        self.assertEqual(rubles_to_words(91_500_007), 'девяноста один миллион пятьсот тысяч семь рублей')

    def test_for_92_601_015(self):
        self.assertEqual(rubles_to_words(92_601_015), 'девяноста два миллиона шестьсот одна тысяча пятнадцать рублей')

    def test_for_95_702_056(self):
        self.assertEqual(rubles_to_words(95_702_056), 'девяноста пять миллионов семьсот две тысячи пятьдесят шесть рублей')

    def test_for_96_811_400(self):
        self.assertEqual(rubles_to_words(96_811_400), 'девяноста шесть миллионов восемьсот одиннадцать тысяч четыреста рублей')

    def test_for_97_999_765(self):
        self.assertEqual(rubles_to_words(97_999_765), 'девяноста семь миллионов девятьсот девяноста девять тысяч семьсот шестьдесят пять рублей')

    def test_for_200_000_000(self):
        self.assertEqual(rubles_to_words(200_000_000), 'двести миллионов рублей')

    def test_for_301_000_001(self):
        self.assertEqual(rubles_to_words(301_000_001), 'триста один миллион один рубль')

    def test_for_402_000_002(self):
        self.assertEqual(rubles_to_words(402_000_002), 'четыреста два миллиона два рубля')

    def test_for_505_001_017(self):
        self.assertEqual(rubles_to_words(505_001_017), 'пятьсот пять миллионов одна тысяча семнадцать рублей')

    def test_for_610_002_073(self):
        self.assertEqual(rubles_to_words(610_002_073), 'шестьсот десять миллионов две тысячи семьдесят три рубля')

    def test_for_777_004_100(self):
        self.assertEqual(rubles_to_words(777_004_100), 'семьсот семьдесят семь миллионов четыре тысячи сто рублей')

    def test_for_800_009_201(self):
        self.assertEqual(rubles_to_words(800_009_201), 'восемьсот миллионов девять тысяч двести один рубль')

    def test_for_901_015_217(self):
        self.assertEqual(rubles_to_words(901_015_217), 'девятьсот один миллион пятнадцать тысяч двести семнадцать рублей')

    def test_for_918_037_542(self):
        self.assertEqual(rubles_to_words(918_037_542), 'девятьсот восемнадцать миллионов тридцать семь тысяч пятьсот сорок два рубля')

    def test_for_984_600_000(self):
        self.assertEqual(rubles_to_words(984_600_000), 'девятьсот восемьдесят четыре миллиона шестьсот тысяч рублей')

    def test_for_972_513_111(self):
        self.assertEqual(rubles_to_words(972_513_111), 'девятьсот семьдесят два миллиона пятьсот тринадцать тысяч сто одиннадцать рублей')

    def test_for_888_777_666(self):
        self.assertEqual(rubles_to_words(888_777_666), 'восемьсот восемьдесят восемь миллионов семьсот семьдесят семь тысяч шестьсот шестьдесят шесть рублей')

    def test_for_1_000_000_000(self):
        self.assertEqual(rubles_to_words(1_000_000_000), 'один миллиард рублей')

    def test_for_2_000_000_000(self):
        self.assertEqual(rubles_to_words(2_000_000_000), 'два миллиарда рублей')

    def test_for_3_000_000_000(self):
        self.assertEqual(rubles_to_words(3_000_000_000), 'три миллиарда рублей')

    def test_for_7_000_000_000(self):
        self.assertEqual(rubles_to_words(7_000_000_000), 'семь миллиардов рублей')

    def test_for_10_000_000_001(self):
        self.assertEqual(rubles_to_words(10_000_000_001), 'десять миллиардов один рубль')

    def test_for_30_000_000_040(self):
        self.assertEqual(rubles_to_words(30_000_000_040), 'тридцать миллиардов сорок рублей')

    def test_for_43_000_000_052(self):
        self.assertEqual(rubles_to_words(43_000_000_052), 'сорок три миллиарда пятьдесят два рубля')

    def test_for_51_000_000_400(self):
        self.assertEqual(rubles_to_words(51_000_000_400), 'пятьдесят один миллиард четыреста рублей')

    def test_for_66_000_000_444(self):
        self.assertEqual(rubles_to_words(66_000_000_444), 'шестьдесят шесть миллиардов четыреста сорок четыре рубля')

    def test_for_1_000_001_000(self):
        self.assertEqual(rubles_to_words(1_000_001_000), 'один миллиард одна тысяча рублей')

    def test_for_2_000_002_002(self):
        self.assertEqual(rubles_to_words(2_000_002_002), 'два миллиарда две тысячи два рубля')

    def test_for_3_000_013_015(self):
        self.assertEqual(rubles_to_words(3_000_013_015), 'три миллиарда тринадцать тысяч пятнадцать рублей')

    def test_for_11_000_600_500(self):
        self.assertEqual(rubles_to_words(11_000_600_500), 'одиннадцать миллиардов шестьсот тысяч пятьсот рублей')

    def test_for_27_000_843_321(self):
        self.assertEqual(rubles_to_words(27_000_843_321), 'двадцать семь миллиардов восемьсот сорок три тысячи триста двадцать один рубль')

    def test_for_1_001_000_000(self):
        self.assertEqual(rubles_to_words(1_001_000_000), 'один миллиард один миллион рублей')

    def test_for_2_002_000_002(self):
        self.assertEqual(rubles_to_words(2_002_000_002), 'два миллиарда два миллиона два рубля')

    def test_for_3_003_000_003(self):
        self.assertEqual(rubles_to_words(3_003_000_003), 'три миллиарда три миллиона три рубля')

    def test_for_11_011_000_011(self):
        self.assertEqual(rubles_to_words(11_011_000_011), 'одиннадцать миллиардов одиннадцать миллионов одиннадцать рублей')

    def test_for_56_065_000_081(self):
        self.assertEqual(rubles_to_words(56_065_000_081), 'пятьдесят шесть миллиардов шестьдесят пять миллионов восемьдесят один рубль')

    def test_for_72_100_000_000(self):
        self.assertEqual(rubles_to_words(72_100_000_000), 'семьдесят два миллиарда сто миллионов рублей')

    def test_for_75_200_000_002(self):
        self.assertEqual(rubles_to_words(75_200_000_002), 'семьдесят пять миллиардов двести миллионов два рубля')

    def test_for_81_300_000_017(self):
        self.assertEqual(rubles_to_words(81_300_000_017), 'восемьдесят один миллиард триста миллионов семнадцать рублей')

    def test_for_81_400_000_058(self):
        self.assertEqual(rubles_to_words(81_400_000_058), 'восемьдесят один миллиард четыреста миллионов пятьдесят восемь рублей')

    def test_for_90_500_000_100(self):
        self.assertEqual(rubles_to_words(90_500_000_100), 'девяноста миллиардов пятьсот миллионов сто рублей')

    def test_for_91_601_000_202(self):
        self.assertEqual(rubles_to_words(91_601_000_202), 'девяноста один миллиард шестьсот один миллион двести два рубля')

    def test_for_93_715_000_319(self):
        self.assertEqual(rubles_to_words(93_715_000_319), 'девяноста три миллиарда семьсот пятнадцать миллионов триста девятнадцать рублей')

    def test_for_97_631_000_857(self):
        self.assertEqual(rubles_to_words(97_631_000_857), 'девяноста семь миллиардов шестьсот тридцать один миллион восемьсот пятьдесят семь рублей')

    def test_for_100_000_000_000(self):
        self.assertEqual(rubles_to_words(100_000_000_000), 'сто миллиардов рублей')

    def test_for_200_002_002_002(self):
        self.assertEqual(rubles_to_words(200_002_002_002), 'двести миллиардов два миллиона две тысячи два рубля')

    def test_for_500_005_005_005(self):
        self.assertEqual(rubles_to_words(500_005_005_005), 'пятьсот миллиардов пять миллионов пять тысяч пять рублей')

    def test_for_600_015_015_015(self):
        self.assertEqual(rubles_to_words(600_015_015_015), 'шестьсот миллиардов пятнадцать миллионов пятнадцать тысяч пятнадцать рублей')

    def test_for_700_034_034_034(self):
        self.assertEqual(rubles_to_words(700_034_034_034), 'семьсот миллиардов тридцать четыре миллиона тридцать четыре тысячи тридцать четыре рубля')

    def test_for_800_800_800_800(self):
        self.assertEqual(rubles_to_words(800_800_800_800), 'восемьсот миллиардов восемьсот миллионов восемьсот тысяч восемьсот рублей')

    def test_for_901_901_901_901(self):
        self.assertEqual(rubles_to_words(901_901_901_901), 'девятьсот один миллиард девятьсот один миллион девятьсот одна тысяча девятьсот один рубль')

    def test_for_105_105_105_105(self):
        self.assertEqual(rubles_to_words(105_105_105_105), 'сто пять миллиардов сто пять миллионов сто пять тысяч сто пять рублей')

    def test_for_217_217_217_217(self):
        self.assertEqual(rubles_to_words(217_217_217_217), 'двести семнадцать миллиардов двести семнадцать миллионов двести семнадцать тысяч двести семнадцать рублей')

    def test_for_340_340_340_340(self):
        self.assertEqual(rubles_to_words(340_340_340_340), 'триста сорок миллиардов триста сорок миллионов триста сорок тысяч триста сорок рублей')

    def test_for_457_321_692_478(self):
        self.assertEqual(rubles_to_words(457_321_692_478), 'четыреста пятьдесят семь миллиардов триста двадцать один миллион шестьсот девяноста две тысячи четыреста семьдесят восемь рублей')

    def test_for_987_654_321_987(self):
        self.assertEqual(rubles_to_words(987_654_321_987), 'девятьсот восемьдесят семь миллиардов шестьсот пятьдесят четыре миллиона триста двадцать одна тысяча девятьсот восемьдесят семь рублей')


if __name__ == '__main__':
    unittest.main()
