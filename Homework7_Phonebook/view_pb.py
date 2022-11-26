from colorama import init
from colorama import Fore, Style
import tqdm

init()


def start_menu():
    """
    Меню выбора действий
    """
    print(Fore.BLUE + "\n"
                      "Выберите пункт меню: \n"
                      "1 - новая запись;\n"
                      "2 - вывод всего справочника в терминал;\n"
                      "3 - импорт справочника;\n"
                      "4 - экспорт справочника; \n"
                      "0 - выход из программы")
    print(Style.RESET_ALL)


def action_type(action: str):
    """
    Вывод параметров для экспорта или импорта
    :param action: "экспорт"/"импорт"
    :return:
    """
    print(Fore.GREEN + f'\n'
                       f'Выберите формат  для {action} файла: \n'
                       "1 - txt;\n"
                       "2 - csv;\n"
                       "0 - возврат в меню")
    print(Style.RESET_ALL)


def get_value() -> str:
    """
    Выбор пользователя
    :return: number: пункт меню
    """
    number = input("Ваш выбор: ")
    return number


def error_type():
    print("Вы ввели не числовое значение, попробуйте снова!")


def error_number():
    print("Вы выбрали не существующий пункт меню, попробуйте снова!")


def error_file():
    print("Указанный файл не найден, проверьте путь или имя файла")


def enter_name_file() -> str:
    name_file = input("Введите имя файла для сохранения")
    return name_file


def error_field():
    print("Вы ввели пустое поле, попробуете снова!")


def get_new_record(data: str) -> str:
    '''
    Ввод новых данных(ФИО, телефон)
    :param data: ("Имя", "фамилию", "телефон", "описание")
    :return:record: введенные от пользователя данные
    '''
    record = input(f"Введите {data}: ")
    return record


def print_all(catalog: str):
    print("Текущие данные из справочника: ")
    print(Fore.YELLOW + catalog)
    print(Style.RESET_ALL)


def name_file():
    name = input("Введите имя файла: ")
    return name


def success_write():
    print("Данные успешно экспортированы!")


def success_read():
    print("Данные успешно импортированы!")
