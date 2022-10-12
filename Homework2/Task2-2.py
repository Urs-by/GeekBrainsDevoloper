# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Введите целое число: "))
# Костыльный метод 1
list1 = [1]
for i in range(1, n + 1):
    list1.append(i * list1[i - 1])
list1.pop(0)
print(f"Метод 1: {list1}")


# Метод 2
def multip(number):
    res = 1
    for i in range(1, number+1):
        res = res * i
    return res

list2 = []
for i in range(1, n+1):
    list2.append(multip(i))
print(f"Метод 2: {list2}")
