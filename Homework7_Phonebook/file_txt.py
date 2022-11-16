def txt_read_file(name_file: str) -> str:
    '''
    Чтение данных из txt файла
    :param name: имя файла
    :return: данные из справочника
    '''
    temp = ''
    with open(name_file, "r", encoding="UTF8") as file:
        count = 1
        stroke = ''
        for line in file:
            if len(line) > 1:
                if count != 4:
                    stroke += line.strip('\n') + ','
                    count += 1
                else:
                    stroke += line.strip('\n') + ','
                    temp += stroke[:-1]
                    temp += '\n'
                    stroke = ''
                    count = 1
    return temp


def txt_write_file(name: str, catalog: str):
    """
    Запись данных в txt файл
    :param name: имя файла
    :param catalog: данные справочника
    :return:
    """
    with open(name, "w", encoding="UTF8") as file:
        record = catalog.split('\n')
        for i in record:
            field = i.split(',')
            for j in field:
                file.writelines(j + '\n')
                file.writelines('\n')
