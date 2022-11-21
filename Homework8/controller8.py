import view8 as view
import validation8 as validation
import function8 as func


len_list_menu = 7


view.start_menu()
choice = view.get_value()
while choice != "0":
    if not validation.valid_type(choice):
        view.error_type()
    elif not validation.valid_number(choice, len_list_menu):
        view.error_number()
    elif choice == '1':
        func.add_record()
    elif choice == '2':
        func.catalog()
    elif choice == '3':
        func.record()
    elif choice == '4':
        func.update()
    elif choice == '5':
        func.delete()
    elif choice == '6':
        func.export_file()
    elif choice == '7':
        func.import_file()

    choice = view.get_value()
