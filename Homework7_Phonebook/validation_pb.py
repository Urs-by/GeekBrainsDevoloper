import view_pb as view


def valid_type(number: str) -> bool:
    """
    Проверка на тип, число
    :param number: введенный параметр
    :return: bool
    """
    if number.isdigit():
        return True
    else:
        return False


def valid_number(number: str, last: int) -> bool:
    """
    Проверка на совпадение пунктов меню
    :param number: пункт меню
    :return: bool
    """
    if 0 <= int(number) <= last:
        return True
    else:
        return False


def valid_field(number: str) -> bool:
    """
    пРоверка на пусто значение
    :param number: пункт меню
    :return: bool
    """
    if number and number.strip():
        return True
    else:
        return False


def valid_data(last: int) -> int:
    """
    Цикл пока не введен правильный пункт меню
    :return: пункт меню
    """
    while True:
        choice = view.get_value()
        if not valid_type(choice):
            view.error_type()
        elif not valid_number(choice, last):
            view.error_number()
        else:
            return int(choice)


def valid_file(name_file: str) -> bool:
    """
    Проверка на существование файла
    :param name_file: имя файла
    :return:bool
    """
    try:
        file = open(name_file, "r", encoding="UTF8")
    except FileNotFoundError:
        return False
    else:
        file.close()
        return True
