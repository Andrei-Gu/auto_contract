import openpyxl
from docxtpl import DocxTemplate
from docx.opc.exceptions import PackageNotFoundError
from ammount_to_words.main import main as a_t_w


def replacing_forbidden_symbols(text):
    forbidden_symbols = '?:/*"<>|\\'
    for char in forbidden_symbols:
        text = text.replace(char, '')
    return text


def comparing_sets(set_in_document, set_in_xlsx):
    msg_1 = 'В выбранном шаблоне имеются следующие переменные, которые отсутствуют в файле print_contract.xlsx или их значения некорректны:'
    msg_2 = 'При заполнении шаблона эти переменные будут удалены из текста без замены какими-либо значениями'
    set_diff = set_in_document - set_in_xlsx
    if set_diff:
        print(msg_1, *set_diff, msg_2, sep='\n')


def printing_bad_pairs(vars):
    msg_1 = 'В файле print_contract.xlsx у перечисленных ниже переменных отсутствует значение или оно некорректное:'
    msg_2 = 'При заполнении шаблона эти переменные будут удалены из текста без замены какими-либо значениями'
    print(msg_1, *vars, msg_2, sep='\n')


def ammount_to_words_with_parentheses(ammount):
    ammount = a_t_w(ammount)
    if ammount.startswith('Введенн'):
        raise ValueError
    else:
        return '(' + ammount.replace(' рубл', ') рубл')


def reading_lines_from_xlsx():
    workbook = openpyxl.load_workbook(filename='print_contract.xlsx', read_only=True)
    sheet = workbook.active
    row = 1
    while True:
        row_str = str(row)
        key = sheet['B' + row_str].value
        if key is None:
            break
        value = sheet['C' + row_str].value
        row += 1
        yield key, value
    workbook.close()


def reading_context_from_xlsx():
    context = {}
    vars_with_no_or_invalid_values = []

    for var, value in reading_lines_from_xlsx():
        if value is None:
            vars_with_no_or_invalid_values.append(var)
            continue

        if 'date' in var:
            try:
                context[var] = value.strftime('%d.%m.%Y')
                continue
            except Exception:
                vars_with_no_or_invalid_values.append(var)
                continue

        if 'digits' in var:
            try:
                context[var.replace('digits', 'words')] = ammount_to_words_with_parentheses(str(value))
                context[var] = value
                continue
            except ValueError:
                vars_with_no_or_invalid_values.append(var)
                continue

        context[var] = value

    if vars_with_no_or_invalid_values:
        printing_bad_pairs(vars_with_no_or_invalid_values)
    return context


def getting_template_name_and_path():
    text = '''
Введите номер шаблона для заполнения:
1 - договор аренды транспортного средства
2 - доверенность в ГАИ
3 - доверенность в страховую
'''
    docx_templates = {'1': ('templates/template_contract_vehicle_rent.docx', 'contracts/rent/'),
                      '2': ('templates/template_attorney_to_GAI.docx', 'contracts/attorney/GAI/'),
                      '3': ('templates/template_attorney_to_insurance.docx', 'contracts/attorney/insurance/'),
                      }

    while True:
        try:
            return docx_templates[input(text)]
        except KeyError:
            print('Введен некорректный номер шаблона')


def executing_all_actions():
    template_name, path_to_save = getting_template_name_and_path()
    try:
        document = DocxTemplate(template_name)
        vars_set_in_document = document.get_undeclared_template_variables()
    except PackageNotFoundError:
        raise FileNotFoundError

    context = reading_context_from_xlsx()
    vars_set_in_xlsx = set(context.keys())

    comparing_sets(vars_set_in_document, vars_set_in_xlsx)
    try:
        if 'rent' in path_to_save:
            path_to_save = path_to_save + context['vehicle_register_sign'] + '/'
        document_name_parts = (path_to_save,
                               replacing_forbidden_symbols(context['person_2_full_name']),
                               ' документ ',
                               replacing_forbidden_symbols(str(context['contract_number'])),
                               ' от ',
                               context['contract_signing_date'],
                               '.docx',
                               )
    except KeyError:
        print('В файле print_contract.xlsx недостаточно данных для формирования имени документа: гос.номер, ФИО лица 2, номера или даты документа')
        raise OSError

    document_name = ''.join(document_name_parts)
    document.render(context)
    document.save(document_name)
    print('Шаблон заполнен и сохранен в файл:', document_name, sep='\n')


def main():
    messages = {'file_not_found_msg': 'Файл выбранного Вами шаблона или print_contract.xlsx не найден. Проверьте его наличие в папке.',
                'os_error_msg': 'Не удается открыть файл выбранного Вами шаблона или print_contract.xlsx, либо сохранить итоговый файл. Попробуйте снова.',
                'error_msg': 'Ошибка. Подробнее об ошибке: ',
                'restart_msg': 'Скрипт начал работу заново',
                }
    try:
        executing_all_actions()
    except FileNotFoundError:
        print(messages['file_not_found_msg'], messages['restart_msg'])

    except OSError:
        print(messages['os_error_msg'], messages['restart_msg'])

    except Exception as err:
        print(messages['error_msg'], err)
        print(messages['restart_msg'])


info = '''
ВАЖНО!
НЕ удаляйте файл print_contract.xlsx, иначе скрипт не будет работать.
НЕ перемещайте файл print_contract.xlsx в другую папку, иначе скрипт не будет работать.
НЕ изменяйте название файла print_contract.xlsx, иначе скрипт не будет работать.
НЕ создавайте в файле print_contract.xlsx новые лист. Лист должен быть только один.

Все шаблоны Word находятся в папке "templates".
Названия всех шаблонов Word начинаются на "template_". НЕ удаляйте, НЕ перемещайте, НЕ изменяйте их название.

Заполненный документ Word (договор, доверенность и т.д.) сохраняется в папке "contracts".
'''


if __name__ == '__main__':
    print(info)

    while True:
        main()
