import view

def game_over(move_player: str) -> bool:
    """
    если "q" то окончание игры
    :param number: введенное значение
    :return: True / False
    """
    if move_player.lower() == "q":
        return True
    else:
        return False


def valid_type(move_player: str) -> bool:
    """
    Проверка на правильность введенного число
    :param number: введенное значение
    :return: True / False
    """
    if move_player.isdigit():
        return True
    if move_player.lower() == "q":
        view.error_quit()
        return False
    else:
        view.error_type()
        return False


def valid_number(move_player: int) -> bool:
    """
    Проверка на правильность номера ячейки поля
    :param number: введенное значение
    :return: True / False
    """
    if 0 < move_player < 10:
        return True
    else:
        view.error_number()
        return False


def valid_value(move_player: int, list_values: list) -> bool:
    """
    Проверка, что ячейка свободна
    :param number: введенное значение
    :param list_values: список с ходами
    :return: True / False
    """
    if list_values[move_player - 1] == ' ':
        return True
    else:
        view.error_value()
        return False


def valid_len_list(list_fild: list) -> bool:
    """
    Проверка на свободные ячейки
    :param list_fild: список с ходами
    :return: True / False
    """
    if ' ' in list_fild:
        return True
    else:
        return False


def valid_total(move_player: str, list_values: list) -> bool:
    """
    Итоговая проверка
    :param number:введенное значение
    :param list_values:список с ходами
    :return: True / False
    """

    if valid_type(move_player) == False:
        return False
    elif valid_number(int(move_player)) == False:
        return False
    elif valid_value(int(move_player), list_values) == False:
        return False
    else:
        return True
