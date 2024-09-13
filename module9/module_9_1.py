def apply_all_func(int_list, *functions):
    result = {}
    for func in functions:
        try:
            result[func.__name__] = func(int_list)
        except TypeError as err:
            print(f'Неверный тип данных - {err}')
    return result

print(apply_all_func([6, '20', 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))