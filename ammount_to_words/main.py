from decimal import Decimal, ROUND_HALF_UP, InvalidOperation


def getting_declension(num, declensions):
    temp_num = num % 10
    if num in (0, 11, 12, 13, 14):
        return declensions[2]
    if temp_num == 1:
        return declensions[0]
    if temp_num in (2, 3, 4):
        return declensions[1]
    return declensions[2]


def pences_to_string(num):
    return str(num // 10) + str(num % 10)


def pences_to_words(ammount):
    declensions = ('копейка', 'копейки', 'копеек')
    words = [pences_to_string(ammount),
             getting_declension(ammount, declensions)
             ]
    return ' '.join(words)


def two_digits_to_words(num, num_class):
    if num_class == 1:
        gender = 'female'
    else:
        gender = 'male'

    ones_1_2 = {'male': {1: 'один',
                         2: 'два',
                         },
                'female': {1: 'одна',
                           2: 'две',
                           },
                }
    
    ones_and_teens = {3: 'три',
                      4: 'четыре',
                      5: 'пять',
                      6: 'шесть',
                      7: 'семь',
                      8: 'восемь',
                      9: 'девять',
                      10: 'десять',
                      11: 'одиннадцать',
                      12: 'двенадцать',
                      13: 'тринадцать',
                      14: 'четырнадцать',
                      15: 'пятнадцать',
                      16: 'шестнадцать',
                      17: 'семнадцать',
                      18: 'восемнадцать',
                      19: 'девятнадцать',
                      }
 
    tens = {2: 'двадцать',
            3: 'тридцать',
            4: 'сорок',
            5: 'пятьдесят',
            6: 'шестьдесят',
            7: 'семьдесят',
            8: 'восемьдесят',
            9: 'девяноста',
            }
    
    words = []
    
    ones_digit = num % 10
    tens_digit = num // 10
    
    if num < 3:
        words.append(ones_1_2[gender][num])
    elif num < 20:
        words.append(ones_and_teens[num])
    else:
        if ones_digit > 0:
            if ones_digit < 3:
                words.append(ones_1_2[gender][ones_digit])
            else:
                words.append(ones_and_teens[ones_digit])
        words.append(tens[tens_digit])
    return words   


def three_digits_to_words(num, num_class):
    hundreds = {1: 'сто',
                2: 'двести',
                3: 'триста',
                4: 'четыреста',
                5: 'пятьсот',
                6: 'шестьсот',
                7: 'семьсот',
                8: 'восемьсот',
                9: 'девятьсот',
                }

    words = []

    num_tail = num % 100
    if num_tail > 0:
        words += two_digits_to_words(num_tail, num_class)
    
    hundreds_digit = num // 100
    if hundreds_digit > 0:
        words.append(hundreds[hundreds_digit])

    words = words[: : -1]
    return ' '.join(words)
    

def rubles_to_words(ammount):
    if ammount == 0:
        return 'ноль рублей'

    words_tail = getting_declension(ammount % 100, ('рубль', 'рубля', 'рублей'))
    
    num_class_declensions = {1: ('тысяча', 'тысячи', 'тысяч'),
                             2: ('миллион', 'миллиона', 'миллионов'),
                             3: ('миллиард', 'миллиарда', 'миллиардов'),
                             }
    
    num_words = []
    temp_words = []
    num_class = 0

    while ammount > 0:
        num_tail = ammount % 1000
        if num_tail > 0:
            temp_words.append(three_digits_to_words(num_tail, num_class))
            if num_class > 0:
                temp_words.append(getting_declension(num_tail % 100,
                                                     num_class_declensions[num_class]
                                                     )
                                  )
            num_words.append(' '.join(temp_words))
            temp_words = []
        ammount = ammount // 1000
        num_class += 1

    num_words = num_words[: : -1]
    num_words.append(words_tail)
    result_words = ' '.join(num_words)
    return result_words


def replacing_commas(some_text):
    return some_text.replace(',', '.')


def replacing_spaces(some_text):
    return some_text.replace(' ', '')


def exceeding_limits(num):
    if num <= 0:
        return True
    if num >= 1_000_000_000_000:
        return True    
    return False


def converting_to_words(ammount):
    result = []

    rubles = int(ammount)
    pences = int((ammount - rubles) * 100)

    result.append(rubles_to_words(rubles))
    result.append(pences_to_words(pences))
    return ' '.join(result)


def main(some_string):
    num = replacing_commas(some_string)
    num = replacing_spaces(num)

    TWOPLACES = Decimal('0.01')
    try:
        ammount = Decimal(num).quantize(TWOPLACES, rounding=ROUND_HALF_UP)
    except InvalidOperation:
        return 'Введенные данные имеют некорректный формат'

    if exceeding_limits(ammount):
        return 'Введенная сумма неположительная или больше/равна 1 000 000 000 000'

    return converting_to_words(ammount)


info = '''
Скрипт позволяет преобразовать введенную сумму в ее словесный эквивалент.
Например,
>>> 1 002 137,11
'один миллион две тысячи сто тридцать семь рублей 11 копеек'
           
Ограничения:
1) вводимая сумма должна быть положительной и меньше 1 000 000 000 000;
2) допускается введение целых или дробных сумм;
3) разделителями целой и дробной части могут выступать символы '.' или ',';
4) допускается указание знака '+' перед суммой;
5) все введенные символы ' ' (пробел) и '_' игнорируются;
6) классы допускается не разделять, либо разделять символами ' ' или '_';
7) вводимая сумма преобразуется в формат Decimal с 2 знаками в дробной части;
8) если в дробной части более 2 знаков, то она будет округлена до 2 знаков с ROUND_HALF_UP;
Примеры ввода:
  +15 (положительное число)
  .11 (дробное число)
  0,11465498 (дробное число)
  6544847.11494 (дробное число)
  1002130 (целое число)
  1002130.0 (целое число)
  1002130,00 (целое число)
  1 002 130 (целое число, символ ' ' разделяет классы)
  1_002_137,11 (символ ',' отделяет дробную часть от целой, а '_' разделяет классы)
     '''

if __name__ == '__main__':
    print(info)
    
    while True:
        print(main(input('Введите сумму: ')))
