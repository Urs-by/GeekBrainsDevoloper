import validation_pb as valid
import view_pb as view
import file_txt as filetxt
import file_csv as filecsv


def new_record(catalog: str, list_menu: list) -> str:
    """
    Запись нового пользователя в catalog
    :param catalog: текущие данные из справочника
    :param list_menu: список полей справочника
    :return: catalog: обновленные данные справочника
    """
    for i in range(len(list_menu)):
        # проверка на пустое значение
        while True:
            new_record = view.get_new_record(list_menu[i])
            if valid.valid_field(new_record):
                break
            else:
                view.error_field()
        catalog += new_record + ','
    # удаляем последнюю запятую из записи
    catalog = catalog[:-1]
    catalog += '\n'
    return catalog


def import_file(name_action: str, catalog: str, last_type_file: int) -> str:
    """
    Импорт данных из файла заданного формата
    :param name_action: название действия-импорт/экспорт
    :param catalog: данные справочника
    :param last_type_file: количество пунктов в меню
    :return: обновленные данные справочника
    """
    view.action_type(name_action)
    number_type = valid.valid_data(last_type_file)
    if number_type == 1:
        name = view.name_file() + '.txt'
        if valid.valid_file(name):
            catalog += filetxt.txt_read_file(name)
            view.success_read()
        else:
            view.error_file()
    elif number_type == 2:
        name = view.name_file() + '.csv'
        if valid.valid_file(name):
            catalog += filecsv.csv_read_file(name)
            view.success_read()
        else:
            view.error_file()
    return catalog


def export_file(name_action: str, catalog: str, last_type_file: int) -> str:
    """
    Экспорт данных в заданный формат
    :param name_action: название действия-импорт/экспорт
    :param catalog: данные справочника
    :param last_type_file: количество пунктов в меню
    :return: обновленные данные справочника
    """
    view.action_type(name_action)
    number_type = valid.valid_data(last_type_file)
    if number_type == 1:
        name = view.name_file() + '.txt'
        filetxt.txt_write_file(name, catalog)
        view.success_write()
    elif number_type == 2:
        name = view.name_file() + '.csv'
        filecsv.csv_write_file(name, catalog)
        view.success_write()
