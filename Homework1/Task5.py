# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# Найдите самостоятельно какая функция стандартной библиотеки вычисляет квадратный корень и как ее можно импортировать в программу
# используйте "Format Specification Mini-Language" для вывода расстояния до второго знака после запятой
import math

ax = int(input("Введите координату Х точки А: "))
ay = int(input("Введите координату Y точки А: "))
bx = int(input("Введите координату Х точки B: "))
by = int(input("Введите координату Y точки B: "))
# применяем теорему Пифагора
print("Решение 1, через теорему Пифагора, где корень квадратный аналогичен возведению в степень 1/2 ")
print('Расстояние между точками А и В = ', round(((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5, 2))
print()

print("Решение 2, через теорему Пифагора, где корень квадратный = стандартной функции math.sqrt()")
print('Расстояние между точками А и В = ', round(math.sqrt((ax - bx) ** 2 + (ay - by) ** 2), 2))
print()
# или
a = [ax, ay]
b = [bx, by]

print("Решение 3, через спец функцию math.dist(a, b)")
print(f"Расстояние между точками А{a} и В{b} = ", "{:.2f}".format(math.dist(a, b)))