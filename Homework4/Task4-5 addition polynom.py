# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Выделите необходимые действия, этапы алгоритма. Посмотрите какие из них уже решены в предыдущей задаче.
# Оформите необходимые функции в виде модуля и импортируйте.
# Примечание Многочлены в файлах могут быть разной степени
from Task4_polynom import write_polynom

# функция чтения данных из файла(без split, для отображения исходных многочленов)
def read(name: str) -> str:
    with open(name, 'r') as file:
        data = file.readline()
    return data


# функция формирует словарь, где ключ -степень, множитель-значение
def dict_data(data: list) -> dict:
    dict_data = {}
    for i in range(1, len(data) - 2):
        if data[i] != '+' or data[i] != '-':
            if 'x^' in data[i]:
                key = int(data[i].split('x^')[1])
                dict_data[key] = int(data[i - 1] + data[i].split('x^')[0])
            elif 'x' in data[i]:
                dict_data[1] = int(data[i - 1] + data[i].split('x')[0])
            elif data[i].isdigit():
                dict_data[0] = int(data[i - 1] + data[i])
    return dict_data


def create_line(val: int, ind: int) -> str:
    sin = ''
    if val > 0:
        sin = '+'
    if ind > 1:
        degr = 'x^'
    elif ind == 1:
        degr = 'x'
        ind = ''
    else:
        degr = ''
        ind = ''
    line = f'{sin}{val}{degr}{ind}'
    return line

# считываем данные из 2х файлов
data1 = read('polynom1.txt')
data2 = read('polynom2.txt')
data_split1 = data1.split()
data_split2 = data2.split()
# формируем словари
dict_data1 = dict_data(data_split1)
dict_data2 = dict_data(data_split2)
# определяем максимальную степень из обоих словарей
max_deegre1 = list(dict_data1.keys())[0]
max_deegre2 = list(dict_data2.keys())[0]
max_deegre = max(max_deegre2, max_deegre1) + 1

new_polynom = ''
for i in reversed(range(max_deegre)):
    # если степень есть в двух многочленах -  суммируем
    if i in dict_data1.keys() and i in dict_data2.keys():
        number = dict_data1[i] + dict_data2[i]
        new_polynom += create_line(number, i)
    # иначе добавляем значения со степенью в суммирующий многочлен
    elif i in dict_data1.keys():
        new_polynom += create_line(dict_data1[i], i)
    elif i in dict_data2.keys():
        new_polynom += create_line(dict_data2[i], i)
new_polynom += '=0'

print("Исходные многочлены: ")
print(data1)
print(data2)
print("Сумма многочленов:")
print(new_polynom)
number = input("Введите порядковый номер файла для записи: ")
name = f'polynom{number}.txt'
write_polynom(name, new_polynom)
print(f"Файл {name} успешно создан!")
