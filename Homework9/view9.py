def input_number(value: str) -> str:
    data = input(f"Введите {value}: ")
    return data


def output(result: list):
    print(result[0], '/', result[1])


def print_result(operation: str):
    if operation == '+':
        print('результатом сложения двух дробей будет:')
    elif operation == '-':
        print('результатом вычитания двух дробей будет:')
    elif operation == '*':
        print('результатом умножения двух дробей будет:')
    elif operation == '/':
        print('результатом деления двух дробей будет:')


list_operation =("+","-","*","/")

def error_operation():
    print("Вы ввели не математический оператор")

