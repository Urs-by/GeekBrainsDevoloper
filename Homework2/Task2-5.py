# Реализуйте алгоритм перемешивания элементов списка.
# Без функции shuffle из модуля random, другие методы использовать можно.
import random

len_n = int(input('Введите длину списка: '))
start_list = list(random.randint(1, 10) for i in range(len_n))

new_list = list(0 for i in range(len_n))

for i in range(len(start_list)):
    while True:
        ind = random.randint(0, len(new_list) - 1)
        if new_list[ind] == 0:
            new_list[ind] = start_list[i]
            break

print("Исходный массив:")
print(start_list)
print("Перемешанный массив:")
print(new_list)