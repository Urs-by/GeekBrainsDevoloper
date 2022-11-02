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
#  Этап 3
#  - Отображение поля с новым состояние и переход хода к следующему игроку.
#  - Проверка текущего состояния системы на "выигрыш" после очередного хода игрока.
#  - Вывод результа о победителе в консоль и указание какая "линия поля" привела к победе:
#    горизонталь, вертикаль, диагональ и какая именно.
#  - (Усложнение. Необязательно) Для индикации победной линии можно использовать https://pypi.org/project/colorama/


import view
import validation
import models

count_players = 2
# # list_values = ['X', 'O', ' ']
list_values = [' ']
numbers = 9
list_field = models.fill_fild(numbers, list_values)

# Ввод игроков
player_one = view.players(1)
player_two = view.players(2)

# Правила игры
print(view.rules_game())

# Розыгрыш первого хода
lotery = models.get_first_move_player(count_players)
if lotery == 1:
    first = player_one
    second = player_two
else:
    first = player_two
    second = player_one
view.start_game(first)

while True:

    move_player = view.move(first)
    # eсли Q то выход
    if validation.game_over(move_player):
        break
    # если введенные параметры верны, записываем Х
    elif models.step(move_player, first, "X", list_field):
        print(view.scheme(list_field))
        win_option = models.victory_option(list_field)
        if validation.valid_option(win_option, "X"):
            view.winner(first)
            print(view.name_list_win(models.number_winner(win_option, "X")))
            break

    # eсли нет пустых ячеек, заканчиваем игру
    if validation.valid_len_list(list_field) == False:
        break
    # переход хода
    move_player = view.move(second)
    if validation.game_over(move_player):
        break
    # если введенные параметры верны, записываем 0
    elif models.step(move_player, second, "0", list_field):
        print(view.scheme(list_field))
        win_option = models.victory_option(list_field)

        if validation.valid_option(win_option, "0"):
            view.winner(second)
            print(view.name_list_win(models.number_winner(win_option, "0")))
            break

view.game_over()
