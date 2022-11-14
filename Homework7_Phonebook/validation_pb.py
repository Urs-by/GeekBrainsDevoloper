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