# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

n = int(input("Введите длинну массива: "))
my_list = [random.randint(1, 100) for i in range(n)]
set_my_list = list(set(my_list))
print("Исходный массив: ")
print(my_list)
print("Список неповторяющихся элементов:")
print(set_my_list)
