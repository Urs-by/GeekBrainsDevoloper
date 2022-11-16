def csv_read_file(name_file: str) -> str:
    """
    Чтение данных из csv файла
    :param file: имя файла
    :return: данные из справочник
    """
    temp = ''
    with open(name_file, "r", encoding="UTF8") as file:
        for line in file:
            if line:
                temp += line
    return temp


def csv_write_file(name: str, catalog: str):
    """
    Запись данных в csv файл
    :param name: имя файла
    :param catalog: данные справочника
    :return:
    """
    with open(name, "w", encoding="UTF8") as file:
        file.writelines(catalog)
