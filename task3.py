import json
import sys


def get_dict_from_arg(i: int) -> dict:
    """
    Функция получения словаря из файла json переданного как аргумент
    в командной строке.
    Возвращает словарь.
    """
    return json.load(open(sys.argv[i]))


def adding_test_result(tests: dict, values: dict):
    """
    Функция добавления результатов тестов путем изменения словаря tests,
    добавлением значений из словаря values.
    Проходит рекурсивно.
    Ничего не возвращает.
    """
    for test in tests:
        for val in values['values']:
            if test.get('id') == val.get('id'):
                test['value'] = val.get('value')
        if 'values' in test.keys():
            adding_test_result(test['values'], values)


def main():
    tests = get_dict_from_arg(1)
    values = get_dict_from_arg(2)
    adding_test_result(tests['tests'], values)
    with open('report.json', 'w') as outfile:
        json.dump(tests, outfile, indent=2)


if __name__ == '__main__':
    main()
