import model_pb as model
import view_pb as view
import validation_pb as valid


def start(last_start_menu: int, last_type_file: int, list_menu: list):

    catalog = ''
    view.start_menu()
    choice = valid.valid_data(last_start_menu)
    while choice != 0:
        if choice == 1:
            catalog = model.new_record(catalog, list_menu)
        elif choice == 2:
            view.print_all(catalog)
        elif choice == 3:
            catalog = model.import_file('импорта', catalog, last_type_file)
        elif choice == 4:
            model.export_file('экспорта', catalog, last_type_file)
        view.start_menu()
        choice = valid.valid_data(last_start_menu)
