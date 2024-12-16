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


if __name__ == '__name__':
    cleared_name = clear_names('names.txt')

    for i in cleared_name:
        print(i)