
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

def custom_write(file_name: str, strings: list):
    str_pos = {}
    line = 1
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        byte = file.tell()
        file.write(f'{string}\n')
        str_pos[(line, byte)] = string
        line += 1
    file.close()
    return str_pos

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)