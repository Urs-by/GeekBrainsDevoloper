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
    if 0 < int(number) <= last:
        return True
    else:
        return False



