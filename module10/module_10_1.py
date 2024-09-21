from threading import Thread
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'a', encoding = 'utf8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end = datetime.now()
print(f'Работа потоков {end - start}')

thr1 = Thread(target = write_words, args = (10, 'example5.txt'))
thr2 = Thread(target = write_words, args = (30, 'example6.txt'))
thr3 = Thread(target = write_words, args = (200, 'example7.txt'))
thr4 = Thread(target = write_words, args = (100, 'example8.txt'))

start = datetime.now()
thr1.start()
thr2.start()
thr3.start()
thr4.start()

thr1.join()
thr2.join()
thr3.join()
thr4.join()

end = datetime.now()
print(f'Работа потоков {end - start}')
