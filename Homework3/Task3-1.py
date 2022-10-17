# 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

n = int(input("Введите длинну массива: "))
my_list = list(random.randint(0, 10) for i in range(n))
print("Исходный массив:")
print(my_list)

summa = 0
print("Сумма элементов списка с нечетными индексами: ")
for i in range(1, len(my_list), 2):
    print(my_list[i], end='  ')
    summa += my_list[i]

print(f'= {summa}')