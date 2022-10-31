import view


def game_over(number: str) -> bool:
    """
    если "q" то окончание игры
    :param number: введенное значение
    :return: True / False
    """
    if number.lower() == "q":
        view.game_over()
        return True
    else:
        return False


def valid_type(number: str) -> bool:
    """
    Проверка на правильность введенного число
    :param number: введенное значение
    :return: True / False
    """
    if number.isdigit():
        return True
    else:
        view.error_type()
        return False


def valid_number(number: int) -> bool:
    """
    Проверка на правильность номера ячейки поля
    :param number: введенное значение
    :return: True / False
    """
    if 0 < number < 10:
        return True
    else:
        view.error_number()
        return False


def valid_value(number: int, list_values: list) -> bool:
    """
    Проверка, что ячейка свободна
    :param number: введенное значение
    :param list_values: список с ходами
    :return: True / False
    """
    if list_values[number - 1] == ' ':
        return True
    else:
        view.error_value()
        return False


def valid_len_list(list_fild: list) -> bool:
    if ' ' in list_fild:
        return True
    else:
        return False


def valid_total(number: str, list_values: list) -> bool:
    """
    Итоговая проверка
    :param number:введенное значение
    :param list_values:список с ходами
    :return:
    """
    if game_over(number):
        return False
    elif valid_type(number) == False:
        return False
    elif valid_number(int(number)) == False:
        return False
    elif valid_value(int(number), list_values) == False:
        return False
    else:
        return True
