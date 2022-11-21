import csv

def get_id() -> int:
    """
    Запрос нна получение последнего ID
    :param name_file: имя файла
    :return: последний ID
    """
    with open('id.txt', 'r') as file:
        number_id = file.readline()
        if not number_id:
            number_id = 0
        else:
            number_id = int(number_id)
    return number_id


def put_id(number_id: str):
    """
    Запись последнего номера ID
    :param name_file: имя файла
    :param number_id: номер ID
    :return: None
    """
    with open('id.txt', 'w') as file:
        file.write(number_id)


def header_csv_file() -> list:
    """
    :return: Возращает заголовки полей
    """
    return ['lastname', 'firstname', 'group']


def read_file(name_file: str, delimiter: str) -> list:
    """
    Считывает данные из csv файла
    :param name_file: имя файла
    :param delimiter: разделитель в csv
    :return: file_data: список с данными из файла
    """
    with open(name_file, encoding='utf-8') as file:
        data = csv.reader(file, delimiter=delimiter)
        file_data = [record for record in data]
    return file_data


def write_db_with_id(db: dict, file_data: list) -> dict:
    """
    Запись в database данных из файла с ID параметрами
    :param db: database
    :param file_data: данные из файла
    :return: обновленный database
    """
    header = header_csv_file()
    for i in file_data:
        db[int(i[0])] = {name: value for name, value in zip(header, i[1:])}
    return db


def write_db_without_id(db: dict, file_data: list) -> dict:
    """
    Запись в database данных из файла без ID
    :param db: database
    :param file_data: данные из файла
    :return: обновленный database
    """
    last_id = get_id() + 1
    header = header_csv_file()
    for i in file_data:
        db[last_id] = {name: value for name, value in zip(header, i)}
        last_id += 1
    put_id(str(last_id - 1))
    return db


# def get_id_from_db(db: dict) -> int:
#     '''
#     Возращает максимальное значение id из db
#     :param db: справочник - database
#     :return: последний id
#     '''
#     return max([int(i) for i in db.keys()])


def new_record_db(db: dict, data: list) -> dict:
    """Запись в database новой записи
    :param db: database
    :param data: данные для записи
    :param last_id: последний ID
    :return: обновленная database
    """
    last_id = get_id() + 1
    header = header_csv_file()
    db[last_id] = {name: value for name, value in zip(header, data)}
    put_id(str(last_id))

    return db


def update_record(db: dict, data: list, user_id: int) -> dict:
    """
    Обновление записи
    :param db: database
    :param data: новые данные для записи
    :param user_id: введенный ID
    :return: обновленную database
    """
    header = header_csv_file()
    db[user_id] = {name: value for name, value in zip(header, data)}
    return db


def delete_record(db: dict, last_id: int) -> dict:
    """
    Удаление записи по ключу
    :param db: database
    :param last_id: значение ключа
    :return: обновленная database
    """
    db.pop(last_id)
    return db


# name = header_csv_file()
# catalog = read_file('catalog.csv', '#')
# database = dict()
# print(catalog)
# db = write_db_with_id(database, catalog)
# print(db)
#
# last_id = str(get_id_from_db(db))
# print(db[last_id])
# print(delet_record(db, last_id))
# # print(db)


def export_db(name_file: str, db: dict):
    """
    Экспорт database в csv afqk
    :param name_file: имя файла
    :param db: database
    :return: None
    """
    with open(name_file, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter='#')
        for key, value in db.items():
            new_rec = []
            new_rec.append(key)
            for item in value.values():
                new_rec.append(item)
            writer.writerow(new_rec)


def read_record(db: dict, user_id: int) -> str:
    """
    Чтение конкретной записи
    :param db: database
    :param user_id: Введенный ID
    :return: требуемую запись
    """
    record = ''
    for i in db[user_id].values():
        record += i + ' '
    return record
