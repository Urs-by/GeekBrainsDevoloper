def valid_type(number: str) -> bool:
    """
    Проверка на тип(число)
    :param number: введенный параметр
    :return: bool
    """
    if number.isdigit():
        return True
    else:
        return False


def valid_number(number: str, last: int) -> bool:
    """
    Проверка на совпадение пунктов меню
    :param number: пункт меню
    :return: bool
    """
    if 0 <= int(number) <= last:
        return True
    else:
        return False


def valid_field(number: str) -> bool:
    """
    проверка на пусто значение
    :param number: пункт меню
    :return: bool
    """
    if number and number.strip():
        return True
    else:
        return False


def valid_id_in_file(name_file: str, delimiter: str) -> bool:
    """
    Определяет есть ли в файле ID
    :param name_file: имя файла
    :param delimiter: разделитель csv файла
    :return: True/False
    """
    with open(name_file, encoding='utf-8') as file:
        data = file.readline().split(delimiter)
        if data[0].isdigit():
            return True
        else:
            return False


#

def valid_id_in_db(db: dict, user_id) -> bool:
    """
    Проверка есть ли запрашиваемый ID в базе
    :param db: database
    :param user_id: Введенный ID
    :return: True/False
    """
    if user_id in db.keys():
        return True
    else:
        return False


def valid_file(name_file: str) -> bool:
    """
    Проверка на существование файла
    :param name_file: имя файла
    :return:bool
    """
    try:
        file = open(name_file, "r", encoding="UTF8")
    except FileNotFoundError:
        return False
    else:
        file.close()
        return True
