#  Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01, 12.00] => 0.19
# Примечание:
#
# Обратите внимание на элемент 5 и и 12.0. Они не участвуют в процессе т.к. дробная часть ноль.
# В списке могут быть как числа float, так и числа int.
# Посмотрите на методы числа float, возможно пригодятся.

import random
# Метод 1 -вводим массив вручную
# float_list = [1.1, 1.2, 3.1, 5, 10.01, 12.00]

#Метод 2 - задаем массив рандомно
n = int(input("Введите длину массива: "))
start_random = 1
stop_random = 20
round_random = 3
float_list = list(round(random.uniform(start_random, stop_random), round_random) for i in range(n))

print("Заданный массив : ")
print(float_list)

new_list = []
for i in range(len(float_list)):
    if float_list[i] % 1 != 0:
        new_list.append(round(float_list[i] % 1, round_random))

print("Разница между максимальным и минимальным значением дробной части элементов массива:")
print(f'{max(new_list)} - {min(new_list)} = {round(max(new_list)-min(new_list),round_random)}')