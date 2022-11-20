def start_menu():
    """
    Меню выбора действий
    """
    print('\n'
          'Выберите пункт меню: \n'
          "1 - Добавить запись;\n"
          "2 - Извлечь запись по ID;\n"
          "3 - Обновить запись по ID;\n"
          "4 - Удалить запись по ID; \n"
          "5 - Export справочника; \n"
          "6 - Import справочника ; \n"
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


def error_field():
    print("Вы ввели пустое поле, попробуете снова!")


def get_new_record(data: str) -> str:
    '''
    Ввод новых данных(ФИО, класс)
    :param data: ("Фамилия", "Имя", "Класс")
    :return:record: введенные от пользователя данные
    '''
    record = input(f"Введите {data}: ")
    return record

def name_file():
    name = input("Введите имя файла: ")
    return name+'.csv'
