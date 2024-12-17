import re
from tkinter.font import names


def clear_names(file_name: str) -> list:
    """ Функция для очистки имён от лишних символов """
    new_names_lict = list()
    with open('data/' + file_name) as names_file:
        namas_list = names_file.read().split()
        for name_item in namas_list:
            new_name = ''
            for symbol in name_item:
                if symbol.isalpha():
                    new_name += symbol
            if new_name.isalpha():
                new_names_lict.append(new_name)
    return new_names_lict


def is_cyuillic(name_item: str) -> bool:
    """ Проверка на вхождение кириллицЫ в строку """
    return bool(re.search( pattern: '[а-яА-Я]', name_item))



def filter_russian_names(names_list: list) -> list:
    """ Фильтрация имён на русском """
    new_names_list = list()
    for name_item in names_list:
        if is_cyuillic(name_item):
            new_names_list.append(names_item)
    return new_names_list


def filter_english_names(names_list: list) -> list:
    """ Фильтрация имён на Английском """
    new_names_list = list()
    for names_item in names_list:
        if not is_cyuillic(name_item):
            new_names_list.append(names_item)
    return new_names_list



def save_to_file(file_name: str, data: str) -> None:
    """ Сохраняет данные в файл """
    with open('data/' + file_name, "w") as names_file:
        names_file.write(data)


if __name__ == '__main__':
    cleared_name = clear_names('names.txt')

    filtered_names = filter_russian_names(cleared_name)
    save_to_file(
        file_name: 'russian_names.txt',
        '\n'.join(filtered_names)
    )

    filtered_names = filter_english_names(cleared_name)
    save_to_file(
        file_name: 'english_names.txt',
        '\n'.join(filtered_names)
    )








