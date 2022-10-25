# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# https://ru.wikipedia.org/wiki/Кодированиедлинсерий
# Создать функцию сжатия строки и функцию восстановления строки.
# Пример:
# ABCDEFGH -> 1A1B1C1D1E1F1G1H -> ABCDEFGH
# WWJJJHDDDDDPPGRRR -> 2W3J1H5D2P1G3R -> WWJJJHDDDDDPPGRRR

def coder(line: str) -> str:
    encoding_line = ''
    count = 1
    temp = line[0]
    for i in range(1, len(line)):
        if line[i] == temp:
            count += 1
        else:
            encoding_line += str(count) + temp
            temp = line[i]
            count = 1
        # кодировка последнего элемента
        if i == (len(line) - 1):
            encoding_line += str(count) + temp
    return encoding_line


def decoder(line: str) -> str:
    decoder_line = ''
    for i in range(0, len(line), 2):
        decoder_line += line[i + 1] * int(line[i])
    return (decoder_line)

line = 'WWJJJHDDDDDPPGRRR'

print("Исходная строка: ", line)
code_line = coder(line)
print("Закодированная строка: ", code_line)
print("Декодированная строка: ", decoder(code_line))