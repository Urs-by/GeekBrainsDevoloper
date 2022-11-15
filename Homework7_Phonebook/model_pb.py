def csv_read_file(name_file: str) -> str:
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


def csv_write_file(name: str, catalog: str):
    '''
    запись данных в csv файл
    :param name: имя файла
    :param catalog: данные для записи
    :return:
    '''
    with open(name, "w", encoding="UTF8") as file:
        file.writelines(catalog)


def txt_write_file(name: str, catalog: str):
    with open(name, "w", encoding="UTF8") as file:
        record = catalog.split('\n')
        for i in record:
            field = i.split(',')
            for j in field:
                file.writelines(j + '\n')
                file.writelines('\n')


def txt_read_file(name_file: str) -> str:
    '''
    чтение данных из txt файла
    :param name: имя файла
    :return:
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
                    stroke=''
                    count = 1


    return temp
