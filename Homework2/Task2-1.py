# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782     -> 23
# - 0,56     -> 11
# - 187,6778 -> 44
# Примечание: Программа должна работать для любого количества цифр в числе)
#


# Решение 1 простое:

n = input("Введите вещественное число: ")
count = 0
for i in n:
    if i.isdigit(): count = count + int(i)
print(f'Сумма цифр числа {n} равна {count}')