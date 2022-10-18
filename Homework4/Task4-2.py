# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Написать функцию, которая принимает аргумент - целое число и возвращает список его простых множителей.
# Пример:
# simple_number(147420) => [2, 3, 5, 7, 13];
# simple_number(374220) => [2, 3, 5, 7, 11];


def simple_number(number):
    simple_list = []
    for i in range(2, number):
        while number % i == 0:
            number /= i
            if i not in simple_list:
                simple_list.append(i)
    return simple_list

number = 147420
print(simple_number(number))