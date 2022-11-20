import view8 as view
import validation8 as validation
import model8 as model

list_field = ["Фамилию", "Имя", "Группу"]
len_list_menu = 7
database = {}


def new_field_record(list_field):
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
        print(database)
    elif choice =='5':
        name_file = view.name_file()
        model.export_db(name_file, database)

    choice = view.get_value()
