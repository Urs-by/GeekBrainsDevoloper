def scheme(field: list):
    """
    Схема игрового поля
    :return: игровое поле с данными
    """
    return f"┌─────┬─────┬─────┐\n" \
           f"|  {field[0]}  |  {field[1]}  |  {field[2]}  |\n" \
           f"├─────┼─────┼─────┤\n" \
           f"|  {field[3]}  |  {field[4]}  |  {field[5]}  |\n" \
           f"├─────┼─────┼─────┤\n" \
           f"|  {field[6]}  |  {field[7]}  |  {field[8]}  |\n" \
           f"└─────┴─────┴─────┘"


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
    :return: номер клетки
    """
    cell_number = input(f"{player}, Ваш ход, введите номер клетки: ")
    return cell_number

def error_type():
    print("Не верный тип данных!")

def error_number():
    print("Вы ввели не существуюший номер ячейки!")

def error_value():
    print("Данная ячейка уже занята!")
    
def game_over():
    print("Игра окончена!")

def start_game(player):
    print(f"{player}, Вы начинаете игру! Ваши крестики ")
