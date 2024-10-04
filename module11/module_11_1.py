import requests
import pandas as pd
import numpy as np
from threading import Thread

def get_request():
    request = requests.get('https://api.github.com/events')
    print('\nRequests')
    print('Status code:', request.status_code)
    print('Data Type:', request.headers['content-type'])
    print('Data:', request.text)

def get_structured_data():
    data = pd.read_csv('pandas-data.csv')
    print('\nPandas')
    print(data)

    average_salary = data['Salary'].mean()
    print('\nAverage Salary: ', average_salary)

    employees = data.shape[0]
    print('\nTotal employees:', employees)


def get_array_calculations():
    print('\nNumpy')
    arr = np.array([
        [2, 3, 1],
        [6, 5, 4]
    ])
    sorter_arr = np.sort(arr)
    print('Sorted array:', sorter_arr)
    print('Array size:', arr.size)

    reversed_arr = np.flip(sorter_arr)
    print('Reversed array:', reversed_arr)


t1 = Thread(target = get_request)
t1.start()

get_structured_data()
get_array_calculations()

t1.join()
