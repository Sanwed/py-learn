def calculate_structure_sum(data):
    res = 0
    for i in data:
        if isinstance(i, int) or isinstance(i, float):
            res += i
        if isinstance(i, str):
            res += len(i)
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            res += calculate_structure_sum(i)
        if isinstance(i, dict):
            list_ = [*dict.keys(i), *dict.values(i)]
            res += calculate_structure_sum(list_)
    return res


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
