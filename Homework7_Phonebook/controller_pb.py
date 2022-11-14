import model_pb as model
import view_pb as view
import validation_pb as valid

last_start_menu = 4
last_type_file = 4
list_menu = ["Имя", "Фамилию", "Телефон", "Описание"]
catalog = ''


def new_record(catalog: str) -> str:
    """
    Запись нового пользователя в temp
    :param temp:
    :return: temp
    """
    for i in range(len(list_menu) - 1):
        new_record = view.get_new_record(list_menu[i])
        catalog += new_record + ','
    catalog += view.get_new_record(list_menu[-1])
    catalog += '\n'
    return catalog


view.start_menu()
choice = valid.valid_data(last_start_menu)
while choice != 0:
    if choice == 1:
        catalog = new_record(catalog)
    elif choice == 2:
        view.print_all(catalog)
    elif choice == 3:
        view.action_type('импорта')
        number_type = valid.valid_data(last_type_file)
        if number_type == 1:
            name = view.name_file() + '.txt'
            catalog += model.txt_read_file(name)
    elif choice == 4:
        view.action_type('экспорта')
        number_type = valid.valid_data(last_type_file)
        if number_type == 1:
            name = view.name_file() + '.txt'
            model.txt_write_file(name, catalog)
    view.start_menu()
    choice = valid.valid_data(last_start_menu)
