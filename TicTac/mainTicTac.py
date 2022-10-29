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


def valid_type(number: str) -> bool:
    """
    Проверка на правильность введенного число
    :param number: введенное значение
    :return: True / False
    """
    if number.isdigit():
        return True
    else:
        return False


def valid_number(number: int) -> bool:
    """
    Проверка на правильность номера ячейки поля
    :param number: введенное значение
    :return: True / False
    """
    if 1 < number < 10:
        return True
    else:
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
        return False


list_values = ['X', 'O', ' ']
numbers = 9
list_field = fill_fild(numbers)
print(view.scheme(list_field))
