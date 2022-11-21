def start_menu():
    """
    Меню выбора действий
    """
    print('Выберите пункт меню: \n'
          "1 - Добавить запись;\n"
          "2 - Вывести в консоль; \n"
          "3 - Извлечь запись по ID;\n"
          "4 - Обновить запись по ID;\n"
          "5 - Удалить запись по ID; \n"
          "6 - Export справочника; \n"
          "7 - Import справочника; \n"
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


def error_id():
    print("Заданного ID нет в справочнике, попробуйте еще раз!")


def error_file():
    print("Указанный файл не найден, проверьте путь или имя файла")


def get_new_record(data: str) -> str:
    """
    Ввод новых данных(ФИО, класс)
    :param data: ("Фамилия", "Имя", "Класс")
    :return:record: введенные от пользователя данные
    """
    record = input(f"Введите {data}: ")
    return record


def name_file():
    name = input("Введите имя файла: ")
    return name + '.csv'


def print_all(db: dict):
    """
    Вывод в консоль текущего справочника
    :param db: database
    :return: None
    """
    print("Текущие данные из справочника: ")
    for key, value in db.items():
        rec = ''
        rec += str(key) + " "
        for item in value.values():
            rec += item + " "
        print(rec)


def get_id_from_user() -> str:
    """
    Запрос ID
    :return: ID
    """
    return input("Ведите ID:  ")


def print_record(rec: str):
    """
    Вывод записи по ID
    :param rec: требунмая запись
    :return: None
    """
    print(rec)


def success_update(user_id: int):
    print(f"Данные с ID {user_id} успешно обновлены!")


def success_deleted(user_id: int):
    print(f"Данные с ID {user_id} успешно удалены!")


def success_import(name_file: str):
    print(f"Данные успешно импортированы из {name_file} файла!")


def success_export(name_file: str):
    print(f"Данные успешно экспортированы в {name_file} файл!")
