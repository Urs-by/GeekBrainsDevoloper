def scheme(field: list) -> str:
    """
    Схема игрового поля
    :return: игровое поле с данными
    """
    print( f"┌─────┬─────┬─────┐\n"
           f"|  {field[0]}  |  {field[1]}  |  {field[2]}  |\n"
           f"├─────┼─────┼─────┤\n"
           f"|  {field[3]}  |  {field[4]}  |  {field[5]}  |\n"
           f"├─────┼─────┼─────┤\n"
           f"|  {field[6]}  |  {field[7]}  |  {field[8]}  |\n"
           f"└─────┴─────┴─────┘")


def rules_game() -> str:
    """
    Правила игры
    :return:
    """
    print( "Для выхода из игры необходимо нажать 'Q'\n"
           "Чтобы поставить крестик/нолик, введите номер клетки согласно схемы:\n"
           "┌─────┬─────┬─────┐ \n"
           "|  1  |  2  |  3  | \n"
           "├─────┼─────┼─────┤ \n"
           "|  4  |  5  |  6  | \n"
           "├─────┼─────┼─────┤ \n"
           "|  7  |  8  |  9  | \n"
           "└─────┴─────┴─────┘")


def players(number_player: int) -> str:
    """
    ВВод имени игрока
    :param number_player: номер игрока
    :return: player: имя игрока
    """
    player = input(f"Игрок {number_player}, Введите Ваше имя: ")
    return player


def move(player: str) -> str:
    """
    Ход игрока
    :param player: Номер игрока
    :return: номер ячейки
    """
    cell_number = input(f"{player}, введите номер ячейки согласно схемы: ")
    return cell_number


def start_game(player):
    print(f"{player}, Вы начинаете игру! Ваши крестики ")


def error_type():
    print("Вы ввели не числовое значение!")


def error_number():
    print("Вы ввели не существуюший номер ячейки!")


def error_value():
    print("Данная ячейка уже занята!")


def error_quit():
    print("Для выхода, сначала закончите ход, потом нажмите 'Q'")


def game_over():
    print("Игра окончена!")

def name_list_win(i):
    name_win=['Выигрышная верхняя горизонталь',
              'Выигрышная средняя горизонталь',
              'Выигрышная нижняя горизонталь',
              'Выигрышная левая вертикаль',
              'Выигрышная средняя вертикаль ',
              'Выигрышная правая вертикаль ',
              'Выигрышная главная диагональ',
              'Выигрышная побочная диагональ']
    return name_win[i]

def winner(player):
    print(f"{player}, Вы победили!")

def win_friendship():
        print("Победила дружба!")

