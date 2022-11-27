def pars(data: str) -> list:
    if '/' in data:
        data_list = (data.split('/'))
    else:
        data_list = [data, 1]
    data_list = list(map(int, data_list))
    return data_list


def nok(fraction1: list, fraction2: list) -> int:
    """
    Функция возвращает наименьшее общее кратное НОК
    :param fraction1: дробь1
    :param fraction2: дробь2
    :return: НОК
    """
    i = max(fraction1[1], fraction2[1])
    while (i % fraction1[1] != 0) or (i % fraction2[1] != 0):
        i += 1
    return i


def cut(fraction: list) -> list:
    """
    Функция сокращения дроби
    :param fraction: дробь
    :return: сокращенная дробь
    """
    for i in range(2, 10):
        while True:
            if fraction[1] % i == 0 and fraction[0] % i == 0:
                fraction[1] = fraction[1] / i
                fraction[0] = fraction[0] / i
            else:
                break
    return list(map(int, fraction))


def calculate(fraction1: list, fraction2: list, operation: str) -> list:
    """
    Вычисление дробей
    :param fraction1: первая дробь
    :param fraction2: вторая дробь
    :param operation: оператор
    :return: реезультат вычисления
    """
    coeff = nok(fraction1, fraction2)
    if operation == '+':
        result = [(coeff / fraction1[1] * fraction1[0]) + (coeff / fraction2[1] * fraction2[0]), coeff]
        return cut(result)
    elif operation == '-':
        result = [(coeff / fraction1[1] * fraction1[0]) - (coeff / fraction2[1] * fraction2[0]), coeff]
        return cut(result)
    elif operation == '*':
        result = [fraction1[0] * fraction2[0], fraction1[1] * fraction2[1]]
        return cut(result)
    elif operation == '/':
        result = [fraction1[0] * fraction2[1], fraction1[1] * fraction2[0]]
        return cut(result)
