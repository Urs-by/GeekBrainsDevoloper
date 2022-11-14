def txt_read_file(name_file: str) -> str:
    """
    Чтение данных из файла
    :param file: имя файла
    :return: справочник
    """
    temp = ''
    with open(name_file, "r", encoding="UTF8") as file:
        for line in file:
            if line:
                temp += line
    return temp


def txt_write_file(name: str, catalog: str):
    with open(name, "w", encoding="UTF8") as file:
        file.writelines(catalog)


