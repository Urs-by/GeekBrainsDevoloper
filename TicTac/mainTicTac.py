#   Написать консольную игру «Крестики-Нолики»
#   Этап 1
#    - Выбор структуры для хранения данных для поля "крестиков-ноликов" 3х3
#    - Наполнение ее случайным состоянием для каждой ячейки: крестик, нолик, пусто
#    - Рисование поля клеток с отображением текущего состояния (frontend в консоли)
#    - Создание frontend модуля: все, что связано с прорисовкой поля. Импорт в основную программу.
#  Этап 2
#   - Интерактивность. Играют два игрока, каждый выбирает ячейку, в которую поставить свой знак(крестик или нолик)
#   - Игроки делают свои ходы пока поле полностью не заполнится, потом выход из программы с соответствующим сообщением.
#   - Полная проверка "на дурака", например, ячейка уже занята. Если используем номера ячеек,
#     то корректность ввода данных от игрока. Вывод значимых и понятных для игрока сообщений о неправильных данных.
#     и возможность ошибаться сколько угодно раз.
#   - Возможность игроку прервать игру в любой момент, "если надоест"
#   - Изменение состояния системы, если ход игрока прошел верификацию
#   - Отображение поля с новым состояние и переход хода к следующему игроку.


import random
import view
import validation


def get_random_values(list_values: list) -> str:
    """
    Случайная генерация крестика/нолик
    :param list_values: список возможных значений
    :return: крестик / нолик / пусто
    """
    return random.choice(list_values)


def fill_fild(number_field: int) -> list:
    """
    Заполнение ячеек случайным состоянием
    :param number_field: количество ячеек
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


def step(player: str, tictac: str) -> list:
    player_move = view.move(player)
    while True:
        if validation.valid_total(player_move, list_field):
            list_field[int(player_move) - 1] = tictac
            return list_field
        else:
            player_move = view.move(player)


count_players = 2
# # list_values = ['X', 'O', ' ']
list_values = [' ']
numbers = 9
list_field = fill_fild(numbers)
player_one = view.players(1)
player_two = view.players(2)
lotery = get_first_move_player(count_players)
if lotery == 1:
    first = player_one
    second = player_two
else:
    first = player_two
    second = player_one
view.start_game(first)
while True:
    if validation.valid_len_list(list_field):
        step(first, "X")
        print(view.scheme(list_field))
    else:
        break
    if validation.valid_len_list(list_field):
        step(second, "0")
        print(view.scheme(list_field))
    else:
        break
view.game_over()