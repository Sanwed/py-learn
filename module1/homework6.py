# Dictionaries

my_dict = {
    'Alex': 2005,
    'Daria': 2006,
    'Anton': 2004,
    'Janna': 2003
}

print('Dict:', my_dict)

print('Existing value:', my_dict.get('Alex'))
print('Not existing value:', my_dict.get('Andrew'))

my_dict['Semen'] = 2000
my_dict['Polina'] = 2005

deleted = my_dict.pop('Daria')
print('Deleted value:', deleted)

print('Edited Dict: ', my_dict)

# Sets

my_set = {1, 'string', 1, 'string', False, (1, 2, 3), (1, 2, 3)}
print('Set:', my_set)

my_set.add(2)
my_set.add(5)
my_set.discard(1)

print('Edited set:', my_set)
