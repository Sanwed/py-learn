def custom_write(file_name, strings):
    string_positions = {}
    file = open(file_name, 'a', encoding = 'utf-8')
    for s in range(len(strings)):
        string_positions[(s + 1, file.tell())] = strings[s]
        file.write(strings[s] + '\n')
    file.close()
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
