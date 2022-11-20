import csv


def get_id() -> int:
    '''
    Запрос нна получение последнего ID
    :param name_file: имя файла
    :return: последний ID
    '''
    with open('id.txt', 'r') as file:
        number_id = int(file.readline())
    return number_id


def put_id(number_id: str):
    '''
    Запись последнего номера ID
    :param name_file: имя файла
    :param number_id: номер ID
    :return: None
    '''
    with open('id.txt', 'w') as file:
        file.write(number_id)


def header_csv_file() -> list:
    '''
    :return: Возращает заголовки полей
    '''
    return ['lastname', 'firstname', 'group']


def read_file(name_file: str, delimiter: str) -> list:
    '''
    Считывает данные из csv файла
    :param name_file: имя файла
    :param delimiter: разделитель в csv
    :return: file_data: список с данными из файла
    '''
    with open(name_file, encoding='utf-8') as file:
        data = csv.reader(file, delimiter=delimiter)
        file_data = [record for record in data]
    return file_data


def write_db_with_id(db: dict, file_data: list) -> dict:
    '''
    Запись в database данных из файла с ID параметрами
    :param db: database
    :param file_data: данные из файла
    :return: обновленный database
    '''
    header = header_csv_file()
    for i in file_data:
        db[i[0]] = {name: value for name, value in zip(header, i[1:])}
    return db


def write_db_without_id(db: dict, file_data: list, last_id: int) -> dict:
    '''
        Запись в database данных из файла без ID
        :param db: database
        :param file_data: данные из файла
        :param last_id: последний ID
        :return: обновленный database
        '''
    header = header_csv_file()
    for i in file_data:
        db[last_id] = {name: value for name, value in zip(header, i)}
        last_id += 1
    return db


def get_id_from_db(db: dict) -> int:
    '''
    Возращает максимальное значение id из db
    :param db: справочник - database
    :return: последний id
    '''
    return max([int(i) for i in db.keys()])


def new_record_db(db: dict, data: list) -> dict:
    '''Запись в database новой записи
    :param db: database
    :param data: данные для записи
    :param last_id: последний ID
    :return: обновленная database
    '''
    last_id = get_id() + 1
    header = header_csv_file()
    db[last_id] = {name: value for name, value in zip(header, data)}
    put_id(str(last_id))
    return db


def delet_record(db: dict, last_id: str) -> dict:
    '''
    Удаление записи по ключу
    :param db: database
    :param last_id: значение ключа
    :return: обновленная database
    '''
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
    with open(name_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='#')



my_dict = {'1': {'lastname': 'a', 'firstname': 'b', 'group': 'c'},
           '2': {'lastname': 'd', 'firstname': 'e', 'group': 'g'}}

record = []
for key, value in my_dict.items():
    record.append(key)
    for val in value.values():
        record.append(val)

print(record)