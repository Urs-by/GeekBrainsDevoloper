import view8 as view
import validation8 as validation
import model8 as model


def new_field_record(list_field: list) -> list:
    """
    Запись нового ученика
    :param list_field: список полей справочника
    :return: new_field данные нового ученика
    """
    new_field = []
    for i in range(len(list_field)):
        # проверка на пустое значение
        while True:
            new_record = view.get_new_record(list_field[i])
            if validation.valid_field(new_record):
                break
            else:
                view.error_field()
        new_field.append(new_record)
    return new_field


def add_record():
    """
    Итоговая функция добавления новой записи
    :return: None
    """
    new_record = new_field_record(list_field)
    model.new_record_db(database, new_record)


def catalog():
    """
    Итоговая функия вывода справочника в консоль
    :return: None
    """
    view.print_all(database)


def record():
    """
    Итоговая функция вывода записи по ID
    :return:
    """
    user_id = int(view.get_id_from_user())
    if validation.valid_id_in_db(database, user_id):
        view.print_record(model.read_record(database, user_id))
    else:
        view.error_id()


def update():
    """
    Итоговая функция замены ученикка
    :return: None
    """
    user_id = int(view.get_id_from_user())
    if validation.valid_id_in_db(database, user_id):
        new_record = new_field_record(list_field)
        model.update_record(database, new_record, user_id)
        view.success_update(user_id)
    else:
        view.error_id()


def delete():
    """
    Итоговая функция удаления записи
    :return: None
    """
    user_id = int(view.get_id_from_user())
    if validation.valid_id_in_db(database, user_id):
        model.delete_record(database, user_id)
        view.success_deleted(user_id)
    else:
        view.error_id()


def export_file():
    """"
    Итоговая функция exporta базы данных
    """
    name_file = view.name_file()
    model.export_db(name_file, database)
    view.success_export(name_file)


def import_file():
    """
    Итоговая функция импорта данных
    :return: None
    """
    name_file = view.name_file()
    # проверка на существование файла
    if validation.valid_file(name_file):
        data_file = model.read_file(name_file, '#')
        # проверка файл с ID или нет
        if validation.valid_id_in_file(name_file, '#'):
            model.write_db_with_id(database, data_file)
            view.success_import(name_file)
        else:
            model.write_db_without_id(database, data_file)
            view.success_import(name_file)
    else:
        view.error_file()


list_field = ["Фамилию", "Имя", "Группу"]
database = {}
