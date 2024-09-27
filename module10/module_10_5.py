from datetime import datetime
from multiprocessing import Pool

def read_info(name: str):
    all_data = []
    with open(name, 'r', encoding = 'utf-8') as file:
        for line in file:
            all_data.append(line)


if __name__ == '__main__':
    files = [f'file-{i}.txt' for i in range(1, 5)]

    start = datetime.now()
    read_info(files[0])
    read_info(files[1])
    read_info(files[2])
    read_info(files[3])
    end = datetime.now()
    print('Линейный подход:', end - start)

    start = datetime.now()

    with Pool(processes = len(files)) as pool:
        pool.map(read_info, files)

    end = datetime.now()
    print('Мультипроцессорный подход:', end - start)
