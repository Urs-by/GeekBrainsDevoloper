# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Примечание:
#
# Алгоритм Негафибоначчи
# Вам понадобится рекурсивный вызов функции или сделайте в виде списка.

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


k = int(input("Введите целое число: "))
fibonachi = []

for i in range(-k, k+1):
    if i < 0:
        fibonachi.append((-1)**(-i+1)*fib(-i))
    elif i == 0:
        fibonachi.append(0)
    else:
        fibonachi.append(fib(i))
print('список негафибоначчи:')
print(fibonachi)