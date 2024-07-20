def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(2)
print_params(2, 'str')
print_params(2, 'str', False)

print_params(b = 25)
print_params(c = [1, 2, 3])


values_list = [1, 'str,', False]
values_dict = {
    'a': 2,
    'b': 'string',
    'c': False
}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, 'str']
print_params(*values_list_2, 42)
