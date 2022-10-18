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


number1 = 147420
number2 = 374220
print(f"Cписок простых множителей для {number1}")
print(simple_number(number1))
print(f"Cписок простых множителей для {number2}")
print(simple_number(number2))
