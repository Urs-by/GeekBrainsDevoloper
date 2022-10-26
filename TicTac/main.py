#   Написать консольную игру «Крестики-Нолики»
#   Этап 1
#    - Выбор структуры для хранения данных для поля "крестиков-ноликов" 3х3
#    - Наполнение ее случайным состоянием для каждой ячейки: крестик, нолик, пусто
#    - Рисование поля клеток с отображением текущего состояния (frontend в консоли)
#    - Создание frontend модуля: все, что связано с прорисовкой поля. Импорт в основную программу.

import random
import view


def get_random_values() -> str:
    """
    Случайная генерация крестика/нолика
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
        list_field[i] = get_random_values()
    return list_field


list_values = ['X', 'O', ' ']
numbers = 9
list_field = fill_fild(numbers)
print(view.scheme(list_field))
