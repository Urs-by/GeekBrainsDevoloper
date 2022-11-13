def start_menu():
    """
    Меню выбора действий
    """
    print('Выберите пункт меню: ')
    print("1 - вывод всего справочника;\n"
          "2 - новая запись;\n"
          "3 - поиск по имени;\n"
          "4 - экспорт справочника в формат html; \n"
          "5 - экспорт справочника в форматы xml \n"
          "0 - выход из программы")


def get_value() -> str:
    """
    Выбор пользователя
    :return: number: пункт меню
    """
    number = input("Ваш выбор: ")
    return number


def error_type():
    print("Вы ввели не числовое значение, попробуйте снова!")


def error_number():
    print("Вы выбрали не существующий пункт меню, попробуйте снова!")


def enter_name_file() -> str:
    name_file = input("Введите имя файла для сохранения")
    return name_file


def get_new_record(data: str) -> str:
    '''
    Ввод новых данных(ФИО, телефон)
    :param data: ("Имя", "фамилию", "телефон", "описание")
    :return:record: введенные от пользователя данные
    '''
    record = input(f"Введите {data}: ")
    return record
