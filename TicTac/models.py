import view
import random
import validation


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
