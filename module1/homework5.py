immutable_var = (1, 'string', True, [1, 2])
print(immutable_var)

# Кортеж не поддерживает обращение к элементам
# immutable_var[0] = 2: Даст TypeError
# Но этот кортеж хранит изменяемый объект - список
immutable_var[-1][0] = 2
print(immutable_var)
# Запись выше не выдаст ошибку и изменит первый элемент в списке

mutable_list = [1, 2, 3]
mutable_list[1] = 'Alex'
print(mutable_list)
