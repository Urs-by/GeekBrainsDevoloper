# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

# n = int(input("Введите длинну массива: "))
# my_list = [random.randint(1, 100) for i in range(n)]
# set_my_list = list(set(my_list))
# print("Исходный массив: ")
# print(my_list)
# print("Список неповторяющихся элементов:")
# print(set_my_list)
pi=3.14159
k = 1
s = 0
i=0

while round(s, 3) != round(pi, 3):

    if i % 2 == 0:
        s += 4/k

    else:
        s -= 4/k
    i += 1
    k += 2

print(i)

print(f"Количество итераций равно {i}")
