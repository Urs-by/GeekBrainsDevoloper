# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

n = int(input('Введите номер четверти: '))
if n < 1 or n > 4:
    print('Вы ввели несуществующий номер четверти!')
else:
    print(f'диапазон возможных координат точек в {n} четверти')
    if n == 1:
        print('x > 0, y > 0')
    elif n == 2:
        print('x < 0, y > 0')
    elif n == 3:
        print('x < 0, y < 0')
    else:
        print('x > 0, y < 0')