import view
import random
import validation
from colorama import Fore


def get_random_values(list_values: list) -> str:
    """
    Случайная генерация крестика/нолик
    :param list_values: список возможных значений
    :return: крестик / нолик / пусто
    """
    return random.choice(list_values)


def fill_fild(number_field: int, list_values: list) -> list:
    """
    Заполнение ячеек случайным состоянием
    :param number_field: количество ячеек
    :param list_values: пустые ячейки
    :return: заполненный список
    """
    list_field = [''] * number_field
    for i in range(len(list_field)):
        list_field[i] = get_random_values(list_values)
    return list_field


def get_first_move_player(count_players) -> int:
    """
    Случайный выбор игрока, который будет ходить первым
    :return: номер игрока (1/2)
    """
    return random.randint(1, count_players)


def step(player_move: str, player: str, tictac: str, list_field: list) -> list:
    """
    Запись хода при условии правиольности введенных данных
    :param player_move: введенный номер ячейеки
    :param player: имя игрока
    :param tictac: крестик или нолик
    :param list_field: список ходов
    :return: list_field: список ходов
    """
    while True:
        if validation.valid_total(player_move, list_field):
            list_field[int(player_move) - 1] = tictac
            return list_field
        else:
            player_move = view.move(player)


def victory_option(field: list) -> list:
    """
    Список с выигрышными вариантами
    :param field: список ходов
    :return: win_option: список с выигрышными вариантами
    """
    win_option = [[field[0], field[1], field[2]],
                  [field[3], field[4], field[5]],
                  [field[6], field[7], field[8]],
                  [field[0], field[3], field[6]],
                  [field[1], field[4], field[7]],
                  [field[2], field[5], field[8]],
                  [field[0], field[4], field[8]],
                  [field[2], field[4], field[6]]]
    return win_option


def number_winner(win_option: list, tictac: str) -> int:
    """
    Определяет индекс выигрышного варианта
    :param win_option: список с выигрышными вариантами
    :param tictac: значение Х или 0
    :return: индекс выигрышного варианта
    """
    for i in range(len(win_option)):
        if win_option[i].count(tictac) == 3:
            return i


def color_index(win_index: int, field_list: list) -> list:
    """
    Закраска выигрышной линии
    :param win_index: индекс выигрышной линии из list_index
    :param field_list: список ходов
    :return: field_list: список ходов с закраской
    """
    list_index = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    color_list = list_index[win_index]
    for i in color_list:
        field_list[i] = Fore.RED + str(field_list[i]) + Fore.RESET
    return field_list
