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




list_field = ["Фамилию", "Имя", "Группу"]
len_list_menu = 7
database = {}
last_id = model.get_id()

view.start_menu()
choice = view.get_value()
while choice != "0":
    if not validation.valid_type(choice):
        view.error_type()
    elif not validation.valid_number(choice, len_list_menu):
        view.error_number()
    elif choice == '1':
        new_record = new_field_record(list_field)
        model.new_record_db(database, new_record)
    elif choice == '2':
        view.print_all(database)
    elif choice == '3':
        user_id = int(view.get_id_from_user())
        if validation.valid_id_in_db(database, user_id):
            view.print_record(model.read_record(database, user_id))
        else:
            view.error_id()
    elif choice == '4':
        user_id = int(view.get_id_from_user())
        if validation.valid_id_in_db(database, user_id):
            new_record = new_field_record(list_field)
            model.update_record(database, new_record, user_id)
            view.success_update(user_id)
        else:
            view.error_id()
    elif choice == '5':
        user_id = int(view.get_id_from_user())
        if validation.valid_id_in_db(database, user_id):
            model.delete_record(database, user_id)
            view.success_deleted(user_id)
        else:
            view.error_id()
    elif choice == '6':
        name_file = view.name_file()
        model.export_db(name_file, database)
        view.success_export(name_file)
    elif choice == '7':
        name_file = view.name_file()
        if validation.valid_file(name_file):
            data_file = model.read_file(name_file, '#')
            if validation.valid_id_in_file(name_file, '#'):
                model.write_db_with_id(database, data_file)
                view.success_import(name_file)
            else:
                model.write_db_without_id(database, data_file)
                view.success_import(name_file)
        else:
            view.error_file()
    # view.start_menu()
    choice = view.get_value()
