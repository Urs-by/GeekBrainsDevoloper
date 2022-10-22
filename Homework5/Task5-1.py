# Напишите программу, удаляющую из текста все слова, содержащие "abc".
# Примечание Текст находится в файле. Его надо считать, текст исправить, исправленный текст записать в новый файл.
# Использовать вложенный менеджер контекста
from functools import reduce


def read_file(name: str) -> str:
    with open(name, 'r') as file:
        data = file.read()
    return data


def write_file(data: str, name: str):
    with open(name, 'w') as file:
        file.writelines(data)


text = read_file('text.txt')
text1 = text.split()
new_list_text = [i for i in text1 if 'abc' not in i]

# метод 1 через  import reduce
new_text1 = reduce(lambda a, b: a + ' ' + b, new_list_text)

# метод 2, классика жанра
new_text2 = ''
for i in new_list_text:
    new_text2 += i+' '

print("Исходный текст:")
print(text)
print("Исправленный текст:")
print(new_text1)
print("или")
print(new_text2)
name = input('Введите имя файла: ')
write_file(new_text1, f'{name}.txt')
print(f"Файл {name}.txt  успешно записан")