# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит некоторое кол-во конфет, например 220.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
# Подумайте об алгоритме игры. Здесь есть ключевые числа количества конфет, которые точно определят победу.
import random


# функция выбора игры
def games(game: int) -> str:
    if game == 1:
        player1 = input("Игрок 1, введите Ваше имя: ")
        player2 = input("Игрок 2, введите Ваше имя: ")
        if player1 == player2:
            player1 += "1"
            player2 += "2"
    elif game == 2:
        print("Привет меня зовут Конфетбот, давай играть")
        player1 = input("Введите Ваше имя: ")
        player2 = "Конфетбот"
    return player1, player2


# жеребьевка
def lottery(player1: str, player2: str) -> str:
    first = player1
    second = player2
    while True:
        throw1 = random.randint(1, 6)
        throw2 = random.randint(1, 6)
        print(f"{player1} у Вас выпало {throw1}, {player2} у Вас выпало {throw2}")
        if throw1 > throw2:
            print(f"{player1}, Вы начинаете игру")
            break
        elif throw1 < throw2:
            print(f"{player2}, Вы начинаете игру")
            first = player2
            second = player1
            break
    return first, second


# функция возвращает количество забранных конфет для бота и для игрока
def move_player(player: str, oponent_move: int) -> int:
    if player == "Конфетбот":
        if oponent_move == 0:
            move = candies % (count + 1)
        else:
            move = (count + 1) - oponent_move
        print(f"Конфетбот: Я забираю {move} конфет")
        return move
    else:
        while True:
            move = int(input(f"{player}, сколько конфет Вы забираете? "))
            if 0 < move < 29:
                return move
            else:
                print(f"По условию задачи вы должны забрать не больше {count} конфет ")


candies = 160
count = 28
one_move = candies % (count + 1)

oponent_move = 0

game = int(input("Для игры с реальным соперником нажмите 1, для игры с ботом нажмите 2 "))
player1, player2 = games(game)
first, second = lottery(player1, player2)
print(f"Подсказка: Оптимальный ход = {one_move}")

while candies > count:
    oponent_move = move_player(first, oponent_move)
    candies -= oponent_move
    print(f"осталось конфет {candies} шт.")
    if candies <= count:
        print(f"{first}, к сожалению, проиграл(а), так как конфет осталось {candies} шт. ")
        break
    oponent_move = move_player(second, oponent_move)
    candies -= oponent_move
    print(f"осталось конфет {candies} шт.")
    if candies <= count:
        print(f"{second}, к сожалению, проиграл(а), так как конфет осталось {candies} шт. ")
