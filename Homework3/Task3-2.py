# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

n = int(input("Введите длинну массива: "))
random_start = 0
random_stop = 10

my_list = list(random.randint(random_start, random_stop) for i in range(n))
print("Исходный массив:")
print(my_list)

if n % 2 == 1:
    len_n = int(n // 2 + 1)
else:
    len_n = int(n / 2)

new_list = []
for i in range(len_n):
    new_list.append(my_list[i] * my_list[-(i + 1)])
print("Произведение пар чисел списка: ")
print(new_list)