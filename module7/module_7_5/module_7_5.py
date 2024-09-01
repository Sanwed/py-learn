import os
import time

directory = os.getcwd()

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(directory, file)
        filetime = round(os.path.getmtime(file))
        formatted_time = time.strftime('%d.%m.%y %H:%M:%S', time.localtime(filetime))
        file_size = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
