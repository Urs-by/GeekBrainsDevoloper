import model9 as model
import view9 as view


def calculation():
    fraction1 = model.pars(view.input_number('значение дроби'))
    fraction2 = model.pars(view.input_number('значение дроби'))
    operation = view.input_number('оператор')
    if operation not in view.list_operation:
        view.error_operation()
    else:
        result = model.calculate(fraction1, fraction2, operation)
        view.print_result(operation)
        view.output(result)


def bot_calculation(data: str):
    if "+" in data:
        operation = "+"
        return model.bot_pars(operation, data)
    elif "-" in data:
        operation = "-"
        return model.bot_pars(operation, data)
    elif "*" in data:
        operation = "*"
        return model.bot_pars(operation, data)
    elif "/" in data:
        operation = "/"
        return model.bot_pars(operation, data)
